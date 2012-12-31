# -*- coding: utf-8 -*-
from unittest import TestCase, main

from codecs import register_error

def handle_unicode_decode_error(e):
    part = e.object[e.start:e.end]
    return (part.decode(e.encoding, "replace").replace(u"\uFFFD", "?"), e.end)

def handle_unicode_encode_error(e):
    print "aspdlspdplspl"
    part = e.object[e.start:e.end]
    return (part.encode(e.encoding, "replace").replace(u"\uFFFD", "?"), e.end)

def handle_codec_exception(e):
    if isinstance(e, UnicodeDecodeError):
        return handle_unicode_decode_error(e)
    elif isinstance(e, UnicodeEncodeError):
        return handle_unicode_encode_error(e)
    raise e


register_error("strict", handle_codec_exception)


class TestForgivingEncode(TestCase):
    def test_unidecode_replaces_unencodable_chars_with_question_marks(self):
        s = "aèì".decode("ascii")
        self.assertEquals(u"a????", s)

    def test_uniencode_replaces_unencodable_chars_with_question_marks(self):
        s = u"aèì".encode("ascii")
        self.assertEquals("a????", s)


if __name__ == "__main__":
    main()
