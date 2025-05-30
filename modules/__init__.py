# note that this only works since the ./modules directory is known to have no subdirectories
# if a subdirectory is ever added, you will need to account for that package's __all__
# I'm just too lazy to do it

# from importlib import import_module
# from pkgutil import iter_modules

from modules.module0 import module0
from modules.module1 import module1
from modules.module2 import module2
from modules.module3 import module3
from modules.module4 import module4
from modules.module5 import module5
from modules.module6 import module6
__all__ = ["module0", "module1", "module2", "module3", "module4", "module5", "module6"]

# for loader, module_name, is_pkg in iter_modules(__path__):
# 	module = import_module(f"{__name__}.{module_name}")
# 	globals()[module_name] = module
# 	public_symbols = [k for k in dir(module) if not k.startswith("_")]
#
# 	for symbol in public_symbols:
# 		globals()[symbol] = getattr(module, symbol)
#
# 	__all__.extend(public_symbols)

