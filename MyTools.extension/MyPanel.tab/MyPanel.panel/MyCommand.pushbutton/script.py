# coding: utf-8
__title__ = "My C# Tool"
__doc__ = "Chạy DLL từ C#"

import clr
import os
from pyrevit import script

dll_path = os.path.join(os.path.dirname(__file__), "MyTool.dll")
clr.AddReference(dll_path)

from MyNamespace import MyRunner

MyRunner.Run()
