# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from example.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyRecord

from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass
from item_list import ItemList
from item_list_helper import ItemListHelper
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class TextboxListener(with_metaclass(ABCMeta)):
    @abstractmethod
    def update(self, items):
        raise NotImplementedError


class TextboxListenerCallbacksHelper():
    @ffi.callback("void(struct DjinniObjectHandle * , struct DjinniRecordHandle *)")
    def update(cself, items):
        try:
            TextboxListenerHelper.selfToPy(cself).update(CPyRecord.toPy(ItemList.c_data_set, items))
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)

    @ffi.callback("void(struct DjinniObjectHandle * )")
    def __delete(c_ptr):
        assert c_ptr in TextboxListenerHelper.c_data_set
        TextboxListenerHelper.c_data_set.remove(c_ptr)

    @staticmethod
    def _add_callbacks():
        lib.textbox_listener_add_callback_update(TextboxListenerCallbacksHelper.update)

        lib.textbox_listener_add_callback___delete(TextboxListenerCallbacksHelper.__delete)

TextboxListenerCallbacksHelper._add_callbacks()

class TextboxListenerHelper:
    c_data_set = MultiSet()
    @staticmethod
    def toPy(obj):
        if obj == ffi.NULL:
            return None
        # Python Objects can be returned without being wrapped in proxies
        py_handle = lib.get_handle_from_proxy_object_cw__textbox_listener(obj)
        if py_handle:
            assert py_handle in TextboxListenerHelper.c_data_set
            aux = ffi.from_handle(ffi.cast("void * ", py_handle))
            lib.textbox_listener___wrapper_dec_ref(obj)
            return aux
        return TextboxListenerCppProxy(obj)

    @staticmethod
    def selfToPy(obj):
        assert obj in TextboxListenerHelper.c_data_set
        return ffi.from_handle(ffi.cast("void * ",obj))

    @staticmethod
    def fromPy(py_obj):
        if py_obj is None:
            return ffi.NULL
        py_proxy = (py_obj)
        if not hasattr(py_obj, "update"):
            raise TypeError

        bare_c_ptr = ffi.new_handle(py_proxy)
        TextboxListenerHelper.c_data_set.add(bare_c_ptr)
        wrapped_c_ptr = lib.make_proxy_object_from_handle_cw__textbox_listener(bare_c_ptr)
        return wrapped_c_ptr