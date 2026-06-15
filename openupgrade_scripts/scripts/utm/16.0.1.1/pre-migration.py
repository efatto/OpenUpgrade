from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    # pre-migration of module base converted name column from utm_campaign
    # into jsonb, hence it suffices to copy the name column into title.
    openupgrade.copy_columns(env.cr, {"utm_campaign": [("name", "title", "jsonb")]})
    # ensure utm_source_unique_name (name is already required)
    langs = env["res.lang"].search([])
    for lang in langs:
        lang_code = lang.code
        env.cr.execute(
            f"""
                UPDATE utm_source SET name = name || jsonb_build_object(
                    '{lang_code}', (name->>'{lang_code}') || '_' || id::text
                ) WHERE id NOT IN (
                    SELECT MIN(id) FROM utm_source GROUP BY name->>'{lang_code}'
                ) AND name ? '{lang_code}'
            """
        )
