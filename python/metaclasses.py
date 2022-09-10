from django.db import models


FORMATS = [
    "bmp",
    "cgimage",
    "canon",
    "dot",
    "gv",
    "xdot",
    "xdot1.2",
    "xdot1.4",
    "eps",
    "exr",
    "fig",
    "gd",
    "gd2",
    "gif",
    "gtk",
    "ico",
    "cmap",
    "ismap",
    "imap",
    "cmapx",
    "imap_np",
    "cmapx_np",
    "jpg",
    "jpeg",
    "jpe",
    "jp2",
    "json",
    "json0",
    "dot_json",
    "xdot_json",
    "pdf",
    "pic",
    "pct",
    "pict",
    "plain",
    "plain-ext",
    "png",
    "pov",
    "ps2",
    "psd",
    "sgi",
    "svg",
    "svgz",
    "tga",
    "tif",
    "tiff",
    "tk",
    "vml",
    "vmlz",
    "vrml",
    "wbmp",
    "webp",
    "xlib",
    "x11",
]


class FormatMetaClass(type):
    def __init__(cls, *args, **kwargs):
        format_choices = set()
        for fmt in FORMATS:
            val = fmt
            attr = val.upper()
            setattr(cls, attr, val)
            format_choices.add((attr, val))

        setattr(cls, "FORMAT_CHOICES", list(format_choices))
        super().__init__(*args, **kwargs)


class FinalMeta(models.base.ModelBase, FormatMetaClass):
    pass


class MigrationSnapshot(models.Model, metaclass=FinalMeta):
    pass
