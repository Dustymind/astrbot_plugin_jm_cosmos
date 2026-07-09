"""
文件名生成器模块 - 简单的密码后缀功能
"""

import random

def generate_album_filename(
    album_id: str,
    password: str = "",
    chapter_idx: int | None = None,
    show_password: bool = False,
) -> str:
    """
    生成下载文件名

    Args:
        album_id: 本子ID
        password: 打包密码
        chapter_idx: 章节序号 (仅章节下载时传入)
        show_password: 是否显示密码提示

    Returns:
        生成的文件名 (不含扩展名)
    """

    hardcoded_classname_list = ['思想道德修养与法律基础', '幻想乡近现代史纲要', '马克思主义基本原理与自然辩证法基本原理', '结界理论基础概论', '形势与政策', '计算机式神应用基础', '大学体育', '大学生心理健康教育', '军事基础', '职业生涯规划', '就业指导与创新创业基础', '幻想乡博丽概论', '基础化学', '有机化学', '医用高等数学', '医学物理学', '医学伦理学', '八云紫传统医学药理学基础', '八云紫传统医学诊断学概论', '传统生药学与法森森林类采集', '方剂学', '内经与伤寒论', '月都传统制药用药理论', '系统解剖学', '组织学与胚胎学', '生理学', '生物化学与分子生物学', '医学细胞生物学', '医学免疫学', '乡内病原生物学', '人体寄生虫学', '病理学', '药理学', '诊断学', '病理生理学', '局部解剖学与断层解剖学', '月都医学科技与临床医技学', '内科学', '外科学', '妇产科学', '儿科学', '骨伤科学', '耳鼻咽喉科学', '眼科学', '口腔医学', '神经病学', '精神病学', '皮肤病与性病学', '传统临床治法', '方向提高课（月都医药科研提高方向）', '方向提高课（永远亭临床提高方向）', '中期永远亭临床教学实习', '永远亭毕业临床实习', '临床技能培训', '临床预备课', '毕业与转段考试', '幻想乡医学史', '月都-永远亭医学史', '大学语文与医古文', '预防医学', '流行病学与循证医学', '临床科研设计、衡量、评价', '急诊与灾难医学', '核医学', '医学统计学', '卫生法学', '麻醉学基础', '医患沟通', '第二课堂综合素质学分', '公共任选课学分', '劳动课']
    random_classname = hardcoded_classname_list[random.randint(0, 70)]
    
    # 基础格式: ID_timestamp 或 ID_chN_timestamp
    if chapter_idx is not None:
        name = f"{random_classname}_{album_id}_Ch{chapter_idx}"
    else:
        name = f"{random_classname}_{album_id}"

    # 可选：添加密码提示
    if show_password and password:
        name += f"#PW{password}"

    return name
