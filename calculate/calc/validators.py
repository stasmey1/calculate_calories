from django.core.validators import ValidationError


def validate_height_weight_age(value: int):
    if not isinstance(value, int):
        raise ValidationError('Допускаются только целые числа', code='no_int')
    if value not in range(1, 221):
        raise ValidationError('Допускаются только значения от 1 до 220', code='out_of_range')
