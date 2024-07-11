from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_enviroment

deep_update(globals(), get_settings_from_enviroment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821



