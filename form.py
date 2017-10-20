#!/usr/bin/env python
"""Form validation by WTForms."""
from wtforms import Form, StringField, IntegerField, DecimalField
from wtforms.validators import (DataRequired, InputRequired, Optional, Length,
                                Regexp)


class UserForm(Form):
    """Used for Customer and Employee data."""
    name = StringField("Name", [DataRequired(), Length(max=30)])


class ProductForm(Form):
    """Used for adding/modifying Products."""
    name = StringField("Name", [DataRequired(), Length(max=30)])
    quantity = IntegerField("Quantity", [InputRequired()])
    price = DecimalField("Price", [InputRequired()])
    provider = StringField("Name", [Optional(), Length(max=30)])
    provider_contact = StringField("Name",
                                   [Optional(), Length(max=12),
                                    Regexp("\d{3}(\.|\-)\d{3}(\.|\-)\d{4}",
                                           message="Format: XXX-XXX-XXXX")])
