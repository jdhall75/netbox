from functools import partial, partialmethod, wraps
from typing import List

import django_filters
import strawberry
import strawberry_django
from strawberry import auto
from utilities.fields import ColorField
from utilities.filters import *


def autotype_decorator(filterset):

    def show_field(fieldname, v, cls):
        print(f"cls: {cls}")
        print(f"{fieldname}: {v}")

    def wrapper(cls):
        cls.filterset = filterset
        fields = filterset.get_fields()
        model = filterset._meta.model
        for fieldname in fields.keys():
            attr_type = auto
            if fieldname not in cls.__annotations__:
                field = model._meta.get_field(fieldname)
                if isinstance(field, ColorField):
                    attr_type = List[str] | None

                cls.__annotations__[fieldname] = attr_type

        declared_filters = filterset.declared_filters
        for fieldname, v in declared_filters.items():
            create_function = False
            attr_type = None

            # NetBox Filter types - put base classes after derived classes
            if isinstance(v, ContentTypeFilter):
                create_function = True
                attr_type = str | None
            elif isinstance(v, MACAddressFilter):
                show_field("MACAddressFilter", v, cls)
            elif isinstance(v, MultiValueArrayFilter):
                show_field("MultiValueArrayFilter", v, cls)
            elif isinstance(v, MultiValueCharFilter):
                create_function = True
                attr_type = List[str] | None
            elif isinstance(v, MultiValueDateFilter):
                attr_type = auto
            elif isinstance(v, MultiValueDateTimeFilter):
                attr_type = auto
            elif isinstance(v, MultiValueDecimalFilter):
                show_field("MultiValueDecimalFilter", v, cls)
            elif isinstance(v, MultiValueMACAddressFilter):
                create_function = True
                attr_type = List[str] | None
            elif isinstance(v, MultiValueNumberFilter):
                create_function = True
                attr_type = List[str] | None
            elif isinstance(v, MultiValueTimeFilter):
                show_field("MultiValueTimeFilter", v, cls)
            elif isinstance(v, MultiValueWWNFilter):
                create_function = True
                attr_type = List[str] | None
            elif isinstance(v, NullableCharFieldFilter):
                show_field("NullableCharFieldFilter", v, cls)
            elif isinstance(v, NumericArrayFilter):
                show_field("NumericArrayFilter", v, cls)
            elif isinstance(v, TreeNodeMultipleChoiceFilter):
                create_function = True
                attr_type = List[str] | None

            # From django_filters - ordering of these matters as base classes must
            # come after derived classes so the base class doesn't get matched first
            elif issubclass(type(v), django_filters.OrderingFilter):
                show_field("OrderingFilter", v, cls)
            elif issubclass(type(v), django_filters.BaseRangeFilter):
                show_field("BaseRangeFilter", v, cls)
            elif issubclass(type(v), django_filters.BaseInFilter):
                show_field("BaseInFilter", v, cls)
            elif issubclass(type(v), django_filters.LookupChoiceFilter):
                show_field("LookupChoiceFilter", v, cls)
            elif issubclass(type(v), django_filters.AllValuesMultipleFilter):
                show_field("AllValuesMultipleFilter", v, cls)
            elif issubclass(type(v), django_filters.AllValuesFilter):
                show_field("AllValuesFilter", v, cls)
            elif issubclass(type(v), django_filters.TimeRangeFilter):
                show_field("TimeRangeFilter", v, cls)
            elif issubclass(type(v), django_filters.IsoDateTimeFromToRangeFilter):
                create_function = True
                attr_type = str | None
            elif issubclass(type(v), django_filters.DateTimeFromToRangeFilter):
                create_function = True
                attr_type = str | None
            elif issubclass(type(v), django_filters.DateFromToRangeFilter):
                create_function = True
                attr_type = str | None
            elif issubclass(type(v), django_filters.DateRangeFilter):
                create_function = True
                attr_type = str | None
            elif issubclass(type(v), django_filters.RangeFilter):
                show_field("RangeFilter", v, cls)
            elif issubclass(type(v), django_filters.NumericRangeFilter):
                show_field("NumericRangeFilter", v, cls)
            elif issubclass(type(v), django_filters.NumberFilter):
                show_field("NumberFilter", v, cls)
            elif issubclass(type(v), django_filters.ModelMultipleChoiceFilter):
                create_function = True
                attr_type = List[str] | None
            elif issubclass(type(v), django_filters.ModelChoiceFilter):
                create_function = True
                attr_type = str | None
            elif issubclass(type(v), django_filters.DurationFilter):
                show_field("DurationFilter", v, cls)
            elif issubclass(type(v), django_filters.IsoDateTimeFilter):
                show_field("IsoDateTimeFilter", v, cls)
            elif issubclass(type(v), django_filters.DateTimeFilter):
                attr_type = auto
            elif issubclass(type(v), django_filters.TimeFilter):
                attr_type = auto
            elif issubclass(type(v), django_filters.DateFilter):
                attr_type = auto
            elif issubclass(type(v), django_filters.TypedMultipleChoiceFilter):
                show_field("TypedMultipleChoiceFilter", v, cls)
            elif issubclass(type(v), django_filters.MultipleChoiceFilter):
                create_function = True
                attr_type = List[str] | None
            elif issubclass(type(v), django_filters.TypedChoiceFilter):
                show_field("TypedChoiceFilter", v, cls)
            elif issubclass(type(v), django_filters.ChoiceFilter):
                show_field("ChoiceFilter", v, cls)
            elif issubclass(type(v), django_filters.BooleanFilter):
                create_function = True
                attr_type = bool | None
            elif issubclass(type(v), django_filters.UUIDFilter):
                create_function = True
                attr_type = str | None
            elif issubclass(type(v), django_filters.CharFilter):
                # looks like only used by 'q'
                create_function = True
                attr_type = str | None
            else:
                show_field("unknown type!", v, cls)

            if fieldname not in cls.__annotations__ and attr_type:
                cls.__annotations__[fieldname] = attr_type

            fname = f"filter_{fieldname}"
            if create_function and not hasattr(cls, fname):
                filter_by_filterset = getattr(cls, 'filter_by_filterset')
                setattr(cls, fname, partialmethod(filter_by_filterset, key=fieldname))

        return cls

    return wrapper


@strawberry.input
class BaseFilterMixin:

    def filter_by_filterset(self, queryset, key):
        return self.filterset(data={key: getattr(self, key)}, queryset=queryset).qs
