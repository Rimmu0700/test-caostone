"""initial schema

Revision ID: 0001
Revises:
Create Date: 2026-10-08 10:30:52.979126
"""

from alembic import op
import sqlalchemy as sa


revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.Column("role_name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("role_id", name=op.f("pk_roles")),
        sa.UniqueConstraint("role_name", name=op.f("uq_roles_role_name")),
    )
    op.create_table(
        "species",
        sa.Column("species_id", sa.Integer(), nullable=False),
        sa.Column("scientific_name", sa.String(length=150), nullable=False),
        sa.Column("local_name", sa.String(length=150), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default="true", nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("species_id", name=op.f("pk_species")),
        sa.UniqueConstraint("scientific_name", name=op.f("uq_species_scientific_name")),
    )
    op.create_table(
        "users",
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column(
            "email_verified", sa.Boolean(), server_default="false", nullable=False
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.role_id"],
            name=op.f("fk_users_role_id_roles"),
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_users")),
        sa.UniqueConstraint("email", name=op.f("uq_users_email")),
    )
    op.create_table(
        "audit_logs",
        sa.Column("audit_id", sa.BigInteger(), nullable=False),
        sa.Column("admin_id", sa.BigInteger(), nullable=False),
        sa.Column("action", sa.String(length=50), nullable=False),
        sa.Column("table_name", sa.String(length=100), nullable=False),
        sa.Column("record_id", sa.BigInteger(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["admin_id"],
            ["users.user_id"],
            name=op.f("fk_audit_logs_admin_id_users"),
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("audit_id", name=op.f("pk_audit_logs")),
    )
    op.create_index(
        "ix_audit_logs_admin_id_created_at",
        "audit_logs",
        ["admin_id", "created_at"],
        unique=False,
    )
    op.create_index(
        "ix_audit_logs_table_name_record_id",
        "audit_logs",
        ["table_name", "record_id"],
        unique=False,
    )
    op.create_table(
        "ethnobotany",
        sa.Column("ethnobotany_id", sa.Integer(), nullable=False),
        sa.Column("species_id", sa.Integer(), nullable=False),
        sa.Column("traditional_benefits", sa.Text(), nullable=True),
        sa.Column("plant_parts_used", sa.Text(), nullable=True),
        sa.Column("usage_method", sa.Text(), nullable=True),
        sa.Column(
            "verification_status",
            sa.String(length=30),
            server_default="pending",
            nullable=False,
        ),
        sa.Column("verified_by", sa.BigInteger(), nullable=True),
        sa.Column("verified_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["species_id"],
            ["species.species_id"],
            name=op.f("fk_ethnobotany_species_id_species"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["verified_by"],
            ["users.user_id"],
            name=op.f("fk_ethnobotany_verified_by_users"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("ethnobotany_id", name=op.f("pk_ethnobotany")),
        sa.UniqueConstraint("species_id", name=op.f("uq_ethnobotany_species_id")),
    )
    op.create_table(
        "identification_sessions",
        sa.Column("session_id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("captured_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "session_status",
            sa.String(length=30),
            server_default="pending",
            nullable=False,
        ),
        sa.Column(
            "detection_status",
            sa.String(length=30),
            server_default="pending",
            nullable=False,
        ),
        sa.Column(
            "photo_consent", sa.Boolean(), server_default="false", nullable=False
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.user_id"],
            name=op.f("fk_identification_sessions_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("session_id", name=op.f("pk_identification_sessions")),
    )
    op.create_index(
        "ix_identification_sessions_session_status",
        "identification_sessions",
        ["session_status"],
        unique=False,
    )
    op.create_index(
        "ix_identification_sessions_user_id_created_at",
        "identification_sessions",
        ["user_id", "created_at"],
        unique=False,
    )
    op.create_table(
        "user_profiles",
        sa.Column("profile_id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("full_name", sa.String(length=150), nullable=False),
        sa.Column("photo_url", sa.String(length=500), nullable=True),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.user_id"],
            name=op.f("fk_user_profiles_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("profile_id", name=op.f("pk_user_profiles")),
        sa.UniqueConstraint("user_id", name=op.f("uq_user_profiles_user_id")),
    )
    op.create_table(
        "user_settings",
        sa.Column("setting_id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column(
            "notification_enabled", sa.Boolean(), server_default="true", nullable=False
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.user_id"],
            name=op.f("fk_user_settings_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("setting_id", name=op.f("pk_user_settings")),
        sa.UniqueConstraint("user_id", name=op.f("uq_user_settings_user_id")),
    )
    op.create_table(
        "classification_results",
        sa.Column("classification_id", sa.BigInteger(), nullable=False),
        sa.Column("session_id", sa.BigInteger(), nullable=False),
        sa.Column("species_id", sa.Integer(), nullable=False),
        sa.Column("confidence_score", sa.Numeric(precision=5, scale=4), nullable=False),
        sa.Column("result_status", sa.String(length=30), nullable=False),
        sa.Column("model_name", sa.String(length=100), nullable=False),
        sa.Column("model_version", sa.String(length=50), nullable=False),
        sa.Column(
            "classified_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["identification_sessions.session_id"],
            name=op.f("fk_classification_results_session_id_identification_sessions"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["species_id"],
            ["species.species_id"],
            name=op.f("fk_classification_results_species_id_species"),
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint(
            "classification_id", name=op.f("pk_classification_results")
        ),
        sa.UniqueConstraint(
            "session_id", name=op.f("uq_classification_results_session_id")
        ),
    )
    op.create_index(
        "ix_classification_results_species_id",
        "classification_results",
        ["species_id"],
        unique=False,
    )
    op.create_table(
        "green_pixel_validations",
        sa.Column("validation_id", sa.BigInteger(), nullable=False),
        sa.Column("session_id", sa.BigInteger(), nullable=False),
        sa.Column(
            "green_pixel_ratio", sa.Numeric(precision=5, scale=4), nullable=False
        ),
        sa.Column("threshold", sa.Numeric(precision=5, scale=4), nullable=False),
        sa.Column("validation_status", sa.String(length=30), nullable=False),
        sa.Column(
            "validated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["identification_sessions.session_id"],
            name=op.f("fk_green_pixel_validations_session_id_identification_sessions"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "validation_id", name=op.f("pk_green_pixel_validations")
        ),
        sa.UniqueConstraint(
            "session_id", name=op.f("uq_green_pixel_validations_session_id")
        ),
    )
    op.create_table(
        "images",
        sa.Column("image_id", sa.BigInteger(), nullable=False),
        sa.Column("session_id", sa.BigInteger(), nullable=False),
        sa.Column("image_type", sa.String(length=30), nullable=False),
        sa.Column("storage_url", sa.String(length=500), nullable=False),
        sa.Column("file_format", sa.String(length=20), nullable=False),
        sa.Column("file_size", sa.BigInteger(), nullable=True),
        sa.Column(
            "uploaded_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["identification_sessions.session_id"],
            name=op.f("fk_images_session_id_identification_sessions"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("image_id", name=op.f("pk_images")),
    )
    op.create_index("ix_images_session_id", "images", ["session_id"], unique=False)
    op.create_table(
        "leaf_detections",
        sa.Column("detection_id", sa.BigInteger(), nullable=False),
        sa.Column("session_id", sa.BigInteger(), nullable=False),
        sa.Column("confidence", sa.Numeric(precision=5, scale=4), nullable=False),
        sa.Column("bbox_x", sa.Numeric(precision=10, scale=4), nullable=False),
        sa.Column("bbox_y", sa.Numeric(precision=10, scale=4), nullable=False),
        sa.Column("bbox_width", sa.Numeric(precision=10, scale=4), nullable=False),
        sa.Column("bbox_height", sa.Numeric(precision=10, scale=4), nullable=False),
        sa.Column("detection_status", sa.String(length=30), nullable=False),
        sa.Column("crop_image_url", sa.String(length=500), nullable=True),
        sa.Column(
            "detected_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["identification_sessions.session_id"],
            name=op.f("fk_leaf_detections_session_id_identification_sessions"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("detection_id", name=op.f("pk_leaf_detections")),
        sa.UniqueConstraint("session_id", name=op.f("uq_leaf_detections_session_id")),
    )
    op.create_table(
        "notifications",
        sa.Column("notification_id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("session_id", sa.BigInteger(), nullable=False),
        sa.Column("notification_type", sa.String(length=50), nullable=False),
        sa.Column("title", sa.String(length=150), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("is_read", sa.Boolean(), server_default="false", nullable=False),
        sa.Column(
            "sent_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["identification_sessions.session_id"],
            name=op.f("fk_notifications_session_id_identification_sessions"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.user_id"],
            name=op.f("fk_notifications_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("notification_id", name=op.f("pk_notifications")),
    )
    op.create_index(
        "ix_notifications_user_id_is_read",
        "notifications",
        ["user_id", "is_read"],
        unique=False,
    )
    op.create_table(
        "feedback_corrections",
        sa.Column("feedback_id", sa.BigInteger(), nullable=False),
        sa.Column("classification_id", sa.BigInteger(), nullable=False),
        sa.Column("curator_id", sa.BigInteger(), nullable=False),
        sa.Column("corrected_species_id", sa.Integer(), nullable=False),
        sa.Column("correction_note", sa.Text(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["classification_id"],
            ["classification_results.classification_id"],
            name=op.f(
                "fk_feedback_corrections_classification_id_classification_results"
            ),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["corrected_species_id"],
            ["species.species_id"],
            name=op.f("fk_feedback_corrections_corrected_species_id_species"),
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["curator_id"],
            ["users.user_id"],
            name=op.f("fk_feedback_corrections_curator_id_users"),
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("feedback_id", name=op.f("pk_feedback_corrections")),
    )
    op.create_index(
        "ix_feedback_corrections_classification_id",
        "feedback_corrections",
        ["classification_id"],
        unique=False,
    )
    op.create_table(
        "gradcam_results",
        sa.Column("gradcam_id", sa.BigInteger(), nullable=False),
        sa.Column("classification_id", sa.BigInteger(), nullable=False),
        sa.Column("heatmap_url", sa.String(length=500), nullable=False),
        sa.Column(
            "generated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["classification_id"],
            ["classification_results.classification_id"],
            name=op.f("fk_gradcam_results_classification_id_classification_results"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("gradcam_id", name=op.f("pk_gradcam_results")),
        sa.UniqueConstraint(
            "classification_id", name=op.f("uq_gradcam_results_classification_id")
        ),
    )


def downgrade() -> None:
    op.drop_table("gradcam_results")
    op.drop_index(
        "ix_feedback_corrections_classification_id", table_name="feedback_corrections"
    )
    op.drop_table("feedback_corrections")
    op.drop_index("ix_notifications_user_id_is_read", table_name="notifications")
    op.drop_table("notifications")
    op.drop_table("leaf_detections")
    op.drop_index("ix_images_session_id", table_name="images")
    op.drop_table("images")
    op.drop_table("green_pixel_validations")
    op.drop_index(
        "ix_classification_results_species_id", table_name="classification_results"
    )
    op.drop_table("classification_results")
    op.drop_table("user_settings")
    op.drop_table("user_profiles")
    op.drop_index(
        "ix_identification_sessions_user_id_created_at",
        table_name="identification_sessions",
    )
    op.drop_index(
        "ix_identification_sessions_session_status",
        table_name="identification_sessions",
    )
    op.drop_table("identification_sessions")
    op.drop_table("ethnobotany")
    op.drop_index("ix_audit_logs_table_name_record_id", table_name="audit_logs")
    op.drop_index("ix_audit_logs_admin_id_created_at", table_name="audit_logs")
    op.drop_table("audit_logs")
    op.drop_table("users")
    op.drop_table("species")
    op.drop_table("roles")
