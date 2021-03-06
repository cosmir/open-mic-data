import pytest

import audioset.util as util


@pytest.fixture()
def tf_bytestring():
    return (b"\nv\n\x19\n\x06labels\x12\x0f\x1a\r\n\x0b\x00\xac\x02\xb4\x02"
            b"\xb5\x02\xbc\x02\xc7\x02\n\x1b\n\x08video_id\x12\x0f\n\r\n\x0b"
            b"rmLnozgTQMY\n\x1e\n\x12start_time_seconds\x12\x08\x12\x06\n\x04"
            b"\x00\x00\xf0A\n\x1c\n\x10end_time_seconds\x12\x08\x12\x06\n\x04"
            b"\x00\x00 B\x12\xa0\x01\n\x9d\x01\n\x0faudio_embedding\x12\x89"
            b"\x01\n\x86\x01\n\x83\x01\n\x80\x01\x1b\xac\x18\x00\xee\x8e\xa5"
            b"\x9ct\x9b\xb7\xb8\xc1\xe1\xd5ot~iF\x9d\xcc\xab\xf4\xd1\xca\xcf"
            b"\xa0\t\x00\xea\xf8U\xef\xd8A\xa3g\nE\xff\x00\xf5\xeb\xb8\xbcn6"
            b"\x12\x9cX\x0fa\x8b~ng\xa6\xe3D\xb2\x00g\x1a\xea\x00/\xd0\xa5\xcd"
            b"[|\xffR\x14\x00b\xc6\xff8E\x99\x87\xabN\xe2\x9f\xc0\x86\x00\xce"
            b"\xff\x8cm\x93\xaf^\x88k\x07xp\xff\xe0\xa3\xe5\x00\x86C&,\x84\xba"
            b"\x00\xf1\xfby\xb3k\xcfT\xcd\xc4\x81_n\x83\x94")


def test_filebase():
    assert util.filebase('foo/bar.baz') == 'bar'
    assert util.filebase('foo/bar.baz.whiz') == 'bar.baz'
    assert util.filebase('foo/') == ''
    assert util.filebase('') == ''


def test_safe_makedirs(tmpdir):
    util.safe_makedirs('foo')
    util.safe_makedirs('foo')
    util.safe_makedirs('')


def test_bytestring_to_record(tf_bytestring):
    features, meta = util.bytestring_to_record(tf_bytestring)
    assert features.shape == (1, 128)
    assert len(meta) == 1


def test_load_tfrecord(tfrecords):
    features, meta = util.load_tfrecord(tfrecords[0])
    assert features.std() > 5
    assert len(features) == len(meta)
    assert len(meta) > 10
