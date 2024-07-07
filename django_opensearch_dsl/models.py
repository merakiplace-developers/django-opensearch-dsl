# File is needed for 'DODConfig.config()' to be called.
from django.db.models.fields import PositiveIntegerRelDbTypeMixin, BigIntegerField


class PositiveBigIntegerField(PositiveIntegerRelDbTypeMixin, BigIntegerField):
    description = "Positive big integer"

    def get_internal_type(self):
        return "PositiveBigIntegerField"

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "min_value": 0,
                **kwargs,
            }
        )
