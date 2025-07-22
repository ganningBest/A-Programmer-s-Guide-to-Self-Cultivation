#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧙‍♂️ 程序员修仙等级检测器
Programmer Cultivation Level Checker

通过问卷调查和行为分析，评估程序员的修仙境界等级
"""

import json
import datetime
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class CultivationLevel:
    """修仙境界数据类"""
    name: str
    emoji: str
    level_range: Tuple[int, int]
    description: str
    characteristics: List[str]
    next_level_tips: List[str]

class CultivationLevelChecker:
    """修仙等级检测器"""
    
    def __init__(self):
        self.levels = self._init_levels()
        self.questions = self._init_questions()
    
    def _init_levels(self) -> Dict[str, CultivationLevel]:
        """初始化修仙境界数据"""
        return {
            "练气期": CultivationLevel(
                name="练气期",
                emoji="🌱",
                level_range=(1, 10),
                description="初入编程世界，心性未稳，容易被Bug心魔困扰",
                characteristics=[
                    "经常因为Bug而焦虑不安",
                    "对技术选择感到迷茫",
                    "工作压力较大，容易情绪波动",
                    "缺乏系统的学习方法",
                    "团队协作能力有待提升"
                ],
                next_level_tips=[
                    "建立每日晨起静心诀的习惯",
                    "学习基础的压力管理技巧",
                    "培养系统性学习的方法",
                    "多与同事交流，建立良好关系",
                    "设定小目标，逐步建立信心"
                ]
            ),
            "筑基期": CultivationLevel(
                name="筑基期",
                emoji="🔥",
                level_range=(11, 20),
                description="掌握基础技能，开始建立代码心法",
                characteristics=[
                    "基本掌握主要技术栈",
                    "能够独立完成简单任务",
                    "开始建立工作节奏",
                    "具备基本的问题解决能力",
                    "情绪管理有所改善"
                ],
                next_level_tips=[
                    "深入学习核心技术原理",
                    "培养代码审美和重构能力",
                    "加强团队协作和沟通技巧",
                    "建立个人技术博客或分享",
                    "参与开源项目贡献代码"
                ]
            ),
            "金丹期": CultivationLevel(
                name="金丹期",
                emoji="⚡",
                level_range=(21, 30),
                description="技术纯熟，心境平和，能独当一面",
                characteristics=[
                    "技术能力达到中级水平",
                    "能够独立负责模块开发",
                    "具备良好的心理调节能力",
                    "开始指导新人成长",
                    "工作生活基本平衡"
                ],
                next_level_tips=[
                    "培养系统架构思维",
                    "提升技术决策能力",
                    "加强跨团队协作能力",
                    "建立个人技术影响力",
                    "学习项目管理技能"
                ]
            ),
            "元婴期": CultivationLevel(
                name="元婴期",
                emoji="🌙",
                level_range=(31, 40),
                description="架构思维成熟，能指导他人修炼",
                characteristics=[
                    "具备高级技术能力",
                    "能够设计系统架构",
                    "成为团队技术骨干",
                    "具备培养他人的能力",
                    "心理素质稳定成熟"
                ],
                next_level_tips=[
                    "培养技术领导力",
                    "学习业务理解能力",
                    "提升跨部门沟通技巧",
                    "建立技术团队文化",
                    "探索技术创新方向"
                ]
            ),
            "化神期": CultivationLevel(
                name="化神期",
                emoji="☀️",
                level_range=(41, 50),
                description="技术与管理并重，心如止水",
                characteristics=[
                    "技术专家级别",
                    "具备团队管理能力",
                    "能够做出重要技术决策",
                    "心理抗压能力极强",
                    "成为他人学习的榜样"
                ],
                next_level_tips=[
                    "扩大技术影响力范围",
                    "培养战略思维能力",
                    "建立行业人脉网络",
                    "探索技术商业化应用",
                    "成为技术布道者"
                ]
            ),
            "合体期": CultivationLevel(
                name="合体期",
                emoji="🌟",
                level_range=(51, 60),
                description="行业专家，影响力广泛",
                characteristics=[
                    "行业知名技术专家",
                    "具备战略规划能力",
                    "影响技术发展方向",
                    "心理境界超然物外",
                    "成为行业意见领袖"
                ],
                next_level_tips=[
                    "推动行业技术进步",
                    "培养下一代技术领袖",
                    "探索技术哲学思考",
                    "实现技术理想抱负",
                    "达到工作生活完美融合"
                ]
            ),
            "大乘期": CultivationLevel(
                name="大乘期",
                emoji="🚀",
                level_range=(61, 70),
                description="技术大牛，开创新的修炼法门",
                characteristics=[
                    "技术界传奇人物",
                    "开创新的技术领域",
                    "影响整个行业发展",
                    "心境达到大师级别",
                    "成为技术精神导师"
                ],
                next_level_tips=[
                    "继续推动技术革新",
                    "培养更多技术人才",
                    "探索技术与人文结合",
                    "实现技术理想的最高境界",
                    "为后人留下宝贵财富"
                ]
            ),
            "渡劫期": CultivationLevel(
                name="渡劫期",
                emoji="🌈",
                level_range=(71, 80),
                description="面临职业转型或创业的重大考验",
                characteristics=[
                    "面临重大职业选择",
                    "承担巨大责任压力",
                    "需要突破自我局限",
                    "考验心理承受极限",
                    "决定未来发展方向"
                ],
                next_level_tips=[
                    "保持内心平静和清醒",
                    "寻求导师和朋友支持",
                    "坚持核心价值观不动摇",
                    "用智慧应对各种挑战",
                    "相信自己能够渡过难关"
                ]
            ),
            "仙人境": CultivationLevel(
                name="仙人境",
                emoji="👑",
                level_range=(81, 100),
                description="达到工作与生活的完美平衡",
                characteristics=[
                    "技术与人生完美融合",
                    "工作生活达到理想状态",
                    "心境超脱世俗烦恼",
                    "成为他人向往的榜样",
                    "实现人生最高价值"
                ],
                next_level_tips=[
                    "享受当下的美好时光",
                    "继续帮助他人成长",
                    "探索生命更深层意义",
                    "留下宝贵的人生智慧",
                    "成为永恒的精神财富"
                ]
            )
        }
    
    def _init_questions(self) -> List[Dict]:
        """初始化测试问题"""
        return [
            {
                "id": 1,
                "category": "技术能力",
                "question": "你对当前主要使用的编程语言的掌握程度如何？",
                "options": [
                    {"text": "刚开始学习，经常需要查文档", "score": 1},
                    {"text": "基本语法熟练，能完成简单任务", "score": 3},
                    {"text": "熟练掌握，能独立开发功能模块", "score": 5},
                    {"text": "精通语言特性，能优化性能和架构", "score": 7},
                    {"text": "专家级别，能指导他人和制定标准", "score": 9}
                ]
            },
            {
                "id": 2,
                "category": "心理素质",
                "question": "遇到难以解决的Bug时，你的心理状态如何？",
                "options": [
                    {"text": "非常焦虑，甚至影响睡眠", "score": 1},
                    {"text": "有些紧张，但能坚持调试", "score": 3},
                    {"text": "保持冷静，系统性地分析问题", "score": 5},
                    {"text": "淡定从容，享受解决问题的过程", "score": 7},
                    {"text": "心如止水，将其视为修炼机会", "score": 9}
                ]
            },
            {
                "id": 3,
                "category": "团队协作",
                "question": "在团队项目中，你通常扮演什么角色？",
                "options": [
                    {"text": "主要执行任务，较少参与讨论", "score": 1},
                    {"text": "积极参与，能完成分配的工作", "score": 3},
                    {"text": "能够协调配合，偶尔提出建议", "score": 5},
                    {"text": "经常主导技术讨论和决策", "score": 7},
                    {"text": "团队核心，负责整体规划和指导", "score": 9}
                ]
            },
            {
                "id": 4,
                "category": "学习成长",
                "question": "你如何看待技术学习和个人成长？",
                "options": [
                    {"text": "被动学习，主要应对工作需要", "score": 1},
                    {"text": "有学习意识，但缺乏系统规划", "score": 3},
                    {"text": "主动学习，有明确的成长目标", "score": 5},
                    {"text": "持续学习，并能指导他人成长", "score": 7},
                    {"text": "终身学习，成为他人学习的榜样", "score": 9}
                ]
            },
            {
                "id": 5,
                "category": "工作生活平衡",
                "question": "你的工作与生活平衡状态如何？",
                "options": [
                    {"text": "经常加班，生活被工作占据", "score": 1},
                    {"text": "偶尔加班，但基本能分开工作生活", "score": 3},
                    {"text": "大部分时间能保持良好平衡", "score": 5},
                    {"text": "工作高效，生活丰富多彩", "score": 7},
                    {"text": "工作生活完美融合，享受每一天", "score": 9}
                ]
            },
            {
                "id": 6,
                "category": "压力管理",
                "question": "面对工作压力时，你的应对方式是？",
                "options": [
                    {"text": "容易被压力压垮，影响工作效率", "score": 1},
                    {"text": "能承受一定压力，但会感到疲惫", "score": 3},
                    {"text": "有自己的减压方法，能有效应对", "score": 5},
                    {"text": "将压力转化为动力，越战越勇", "score": 7},
                    {"text": "心境超然，压力对我毫无影响", "score": 9}
                ]
            },
            {
                "id": 7,
                "category": "技术影响力",
                "question": "你在技术社区的参与程度如何？",
                "options": [
                    {"text": "很少参与，主要是被动学习", "score": 1},
                    {"text": "偶尔参与讨论，关注技术动态", "score": 3},
                    {"text": "积极参与，有时分享经验", "score": 5},
                    {"text": "经常分享，在社区有一定影响力", "score": 7},
                    {"text": "技术领袖，引领社区发展方向", "score": 9}
                ]
            },
            {
                "id": 8,
                "category": "心理修炼",
                "question": "你是否有定期的心理调节和自我反思习惯？",
                "options": [
                    {"text": "从不进行，随遇而安", "score": 1},
                    {"text": "偶尔反思，但不够系统", "score": 3},
                    {"text": "有一定习惯，定期自我调节", "score": 5},
                    {"text": "每日修炼，持续自我提升", "score": 7},
                    {"text": "修炼已成自然，时刻保持觉察", "score": 9}
                ]
            }
        ]
    
    def conduct_assessment(self) -> Dict:
        """进行修仙等级评估"""
        print("🧙‍♂️ 欢迎来到程序员修仙等级检测器！")
        print("=" * 50)
        print("请根据你的实际情况，诚实回答以下问题。")
        print("这将帮助你了解当前的修仙境界，并获得针对性的修炼建议。")
        print()
        
        total_score = 0
        category_scores = {}
        
        for question in self.questions:
            print(f"问题 {question['id']}: {question['question']}")
            print()
            
            for i, option in enumerate(question['options'], 1):
                print(f"{i}. {option['text']}")
            
            while True:
                try:
                    choice = int(input("\n请选择 (1-5): "))
                    if 1 <= choice <= 5:
                        score = question['options'][choice-1]['score']
                        total_score += score
                        
                        category = question['category']
                        if category not in category_scores:
                            category_scores[category] = []
                        category_scores[category].append(score)
                        break
                    else:
                        print("请输入1-5之间的数字！")
                except ValueError:
                    print("请输入有效的数字！")
            
            print("-" * 30)
        
        # 计算平均分和等级
        avg_score = total_score / len(self.questions)
        level_info = self._determine_level(avg_score)
        
        # 生成详细报告
        report = self._generate_report(total_score, avg_score, level_info, category_scores)
        
        return report
    
    def _determine_level(self, avg_score: float) -> CultivationLevel:
        """根据平均分确定修仙境界"""
        if avg_score <= 2:
            return self.levels["练气期"]
        elif avg_score <= 3:
            return self.levels["筑基期"]
        elif avg_score <= 4.5:
            return self.levels["金丹期"]
        elif avg_score <= 6:
            return self.levels["元婴期"]
        elif avg_score <= 7:
            return self.levels["化神期"]
        elif avg_score <= 8:
            return self.levels["合体期"]
        elif avg_score <= 8.5:
            return self.levels["大乘期"]
        elif avg_score <= 9:
            return self.levels["渡劫期"]
        else:
            return self.levels["仙人境"]
    
    def _generate_report(self, total_score: int, avg_score: float, 
                        level_info: CultivationLevel, category_scores: Dict) -> Dict:
        """生成详细的评估报告"""
        # 计算各维度得分
        dimension_analysis = {}
        for category, scores in category_scores.items():
            dimension_analysis[category] = {
                "average": sum(scores) / len(scores),
                "total": sum(scores),
                "count": len(scores)
            }
        
        report = {
            "assessment_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_score": total_score,
            "average_score": round(avg_score, 2),
            "cultivation_level": {
                "name": level_info.name,
                "emoji": level_info.emoji,
                "description": level_info.description,
                "characteristics": level_info.characteristics,
                "next_level_tips": level_info.next_level_tips
            },
            "dimension_analysis": dimension_analysis,
            "recommendations": self._generate_recommendations(avg_score, dimension_analysis)
        }
        
        return report
    
    def _generate_recommendations(self, avg_score: float, dimension_analysis: Dict) -> List[str]:
        """生成个性化修炼建议"""
        recommendations = []
        
        # 找出最薄弱的维度
        weakest_dimension = min(dimension_analysis.items(), 
                               key=lambda x: x[1]['average'])
        
        # 根据整体水平给出建议
        if avg_score < 3:
            recommendations.extend([
                "建议从基础修炼开始，每日坚持晨起静心诀",
                "学习基本的压力管理和情绪调节技巧",
                "寻找一位修仙导师或加入修炼小组"
            ])
        elif avg_score < 5:
            recommendations.extend([
                "继续巩固基础，同时开始学习进阶功法",
                "多参与团队协作，提升沟通能力",
                "建立个人技术博客，分享学习心得"
            ])
        elif avg_score < 7:
            recommendations.extend([
                "开始承担更多技术责任，培养领导力",
                "深入学习系统架构和设计模式",
                "指导新人成长，在教学中提升自己"
            ])
        else:
            recommendations.extend([
                "继续保持高水平修炼，成为他人榜样",
                "探索技术创新，推动行业发展",
                "培养更多技术人才，传承修仙文化"
            ])
        
        # 针对薄弱维度的建议
        weak_category = weakest_dimension[0]
        if weak_category == "心理素质":
            recommendations.append("重点加强心理修炼，学习冥想和正念技巧")
        elif weak_category == "团队协作":
            recommendations.append("多参与团队活动，提升沟通和协作能力")
        elif weak_category == "技术能力":
            recommendations.append("加强技术学习，深入掌握核心技能")
        
        return recommendations
    
    def display_report(self, report: Dict):
        """显示评估报告"""
        print("\n" + "="*60)
        print("🎉 修仙等级评估报告")
        print("="*60)
        
        level = report['cultivation_level']
        print(f"\n🏔️ 当前境界: {level['emoji']} {level['name']}")
        print(f"📊 总分: {report['total_score']}/72 (平均分: {report['average_score']}/9)")
        print(f"📅 评估时间: {report['assessment_date']}")
        
        print(f"\n📖 境界描述:")
        print(f"   {level['description']}")
        
        print(f"\n✨ 当前境界特征:")
        for characteristic in level['characteristics']:
            print(f"   • {characteristic}")
        
        print(f"\n🚀 晋升建议:")
        for tip in level['next_level_tips']:
            print(f"   • {tip}")
        
        print(f"\n📈 各维度分析:")
        for category, analysis in report['dimension_analysis'].items():
            stars = "★" * int(analysis['average']) + "☆" * (9 - int(analysis['average']))
            print(f"   {category}: {analysis['average']:.1f}/9 {stars}")
        
        print(f"\n💡 个性化修炼建议:")
        for recommendation in report['recommendations']:
            print(f"   • {recommendation}")
        
        print("\n" + "="*60)
        print("🙏 感谢参与修仙等级评估！")
        print("记住：修仙之路漫长，但每一步都有意义。")
        print("愿你在代码的世界中，心境如仙，技艺超群！")
        print("="*60)

def main():
    """主函数"""
    checker = CultivationLevelChecker()
    
    try:
        report = checker.conduct_assessment()
        checker.display_report(report)
        
        # 可选：保存报告到文件
        save_report = input("\n是否保存评估报告到文件？(y/n): ").lower()
        if save_report == 'y':
            filename = f"cultivation_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            print(f"✅ 报告已保存到: {filename}")
    
    except KeyboardInterrupt:
        print("\n\n👋 修炼之路虽然中断，但随时可以重新开始！")
    except Exception as e:
        print(f"\n❌ 评估过程中出现错误: {e}")
        print("请稍后重试或联系技术支持。")

if __name__ == "__main__":
    main()
