from django import forms
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe


class FontAwesomeIconPicker(forms.widgets.TextInput):
    class Media:
        css = {
            'all': (
                #                 STATIC_URL + 'really-simple-color-picker-master/css/colorPicker.css',
                settings.STATIC_URL + 'css/colorpicker/bootstrap-colorpicker.min.css',
            )
        }
        js = (
            settings.STATIC_URL + 'js/IconPickerjs/fontawesome-iconpicker.js',
            # settings.STATIC_URL + 'js/IconPickerjs/iconpick.js',
        )


    def __init__(self, attrs = None):
        super().__init__(attrs = attrs)

    def render(self, name, value, attrs=None, renderer=None):
        #         rendered = super(FontAwesomeIconPicker, self).render(name, value, attrs)
        #         a = u'<input type="checkbox" data-size="mini" data-off-color="warning" data-on-color="info" data-on-text="فعال" data-off-text="غیرفعال" name="%s" id="id_%s" %s >' % (name, name, value)
        if value is None:
            value = ''
        return mark_safe(u'''

            <input type="text" name="%(name)s" class="form-control icp icp-auto" id="id_%(name)s" value="%(value)s" />
            <script>
                $(document).ready(function(){
                    $('#id_%(name)s').iconpicker();
                    $('#id_%(name)s.icp').on('iconpickerSelected', function(e) {
                        $('#i_%(name)s').get(0).className = 'picker-target fa-2x ' +
                        e.iconpickerInstance.options.iconBaseClass + ' ' +
                        e.iconpickerInstance.getValue(e.iconpickerValue);
                    });

                    //for inline field
                    $('.add-row').click(function(){
                        $(".iconpicker-element").iconpicker();
                    });

                });
            </script>
            <p class="lead">
                <i class="%(value)s fa fa-2x picker-target" id="i_%(name)s"></i>
                ddd
            </p> ''' % {'name': name, 'value': value})


class IconPicker(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = FontAwesomeIconPicker
        return super().formfield(**kwargs)