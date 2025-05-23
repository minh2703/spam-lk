
import importlib.util

spec = importlib.util.spec_from_file_location("zlocket", "zLocket-Tool.pyc")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
