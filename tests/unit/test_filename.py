"""
文件名生成器测试

测试 utils/filename.py 中的 generate_album_filename 函数。

filename.py 无插件内相对导入，直接按文件路径加载，避免触发 utils 包的
__init__.py（其 formatter 依赖插件包层级，独立测试环境无法导入）。
"""

import importlib.util
from pathlib import Path

_FILENAME_PATH = Path(__file__).resolve().parents[2] / "utils" / "filename.py"
_spec = importlib.util.spec_from_file_location("jm_filename_under_test", _FILENAME_PATH)
_filename_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_filename_module)

generate_album_filename = _filename_module.generate_album_filename


class TestGenerateAlbumFilename:
    """文件名生成测试"""

    def test_no_suffix_by_default(self):
        """默认不追加密码提示与时间戳"""
        name = generate_album_filename("123456")
        assert "123456" in name
        assert "#PW" not in name
        assert not name.endswith("-1700000000")

    def test_timestamp_appended_at_end(self):
        """时间戳追加到文件名末尾"""
        name = generate_album_filename("123456", timestamp="1700000000")
        assert name.endswith("-1700000000")

    def test_timestamp_with_password_hint(self):
        """密码提示与时间戳同时存在时时间戳在末尾"""
        name = generate_album_filename(
            "123456",
            password="1700000000",
            show_password=True,
            timestamp="1700000000",
        )
        assert "#PW1700000000" in name
        assert name.endswith("-1700000000")

    def test_chapter_filename_with_timestamp(self):
        """章节文件名包含章节号与时间戳"""
        name = generate_album_filename(
            "123456", chapter_idx=3, timestamp="1700000000"
        )
        assert "Ch3" in name
        assert name.endswith("-1700000000")

    def test_empty_timestamp_not_appended(self):
        """时间戳为空时不追加分隔符"""
        name = generate_album_filename("123456", timestamp="")
        assert not name.endswith("-")
