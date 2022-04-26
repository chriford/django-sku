from rolepermissions.roles import AbstractUserRole

class English(AbstractUserRole):
    available_permissions = {
        'can_delete_english_entry': True,
        'can_view_english_entry': True,
        'can_update_english_entry': True,
        'can_create_english_entry': True,
    }

class Physics(AbstractUserRole):
    available_permissions = {
        'can_delete_physics_entry': True,
        'can_view_physics_entry': True,
        'can_update_physics_entry': True,
        'can_create_physics_entry': True,
    }

class Chemistry(AbstractUserRole):
    available_permissions = {
        'can_delete_chemistry_entry': True,
        'can_view_chemistry_entry': True,
        'can_update_chemistry_entry': True,
        'can_create_chemistry_entry': True,
    }

class Biology(AbstractUserRole):
    available_permissions = {
        'can_delete_biology_entry': True,
        'can_view_biology_entry': True,
        'can_update_biology_entry': True,
        'can_create_biology_entry': True,
    }

class Mathematics(AbstractUserRole):
    available_permissions = {
        'can_delete_mathematics_entry': True,
        'can_view_mathematics_entry': True,
        'can_update_mathematics_entry': True,
        'can_create_mathematics_entry': True,
    }

class Geography(AbstractUserRole):
    available_permissions = {
        'can_delete_geography_entry': True,
        'can_view_geography_entry': True,
        'can_update_geography_entry': True,
        'can_create_geography_entry': True,
    }
