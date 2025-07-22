#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
程序员心理健康快速检测工具
Mental Health Quick Checker for Programmers

这是一个简单的命令行工具，帮助程序员快速评估自己的心理健康状态。
"""

import json
import datetime
from typing import Dict, List, Tuple
import os

class MentalHealthChecker:
    """程序员心理健康检测器"""
    
    def __init__(self):
        self.questions = self._load_questions()
        self.results_file = "mental_health_results.json"
    
    def _load_questions(self) -> Dict:
        """加载评估问题"""
        return {
            "stress": {
                "title": "压力水平评估",
                "questions": [
                    "我感到工作压力很大",
                    "我经常担心工作任务无法完成",
                    "我难以在工作后放松",
                    "我感到被工作压垮",
                    "我经常加班到很晚"
                ]
            },
            "mood": {
                "title": "情绪状态评估", 
                "questions": [
                    "我感到沮丧或抑郁",
                    "我对平时感兴趣的事物失去兴趣",
                    "我感到焦虑或紧张",
                    "我容易发怒或烦躁",
                    "我感到孤独"
                ]
            },
            "cognitive": {
                "title": "认知功能评估",
                "questions": [
                    "我难以集中注意力",
                    "我记忆力下降",
                    "我决策困难",
                    "我学习新技术感到困难",
                    "我创造力下降"
                ]
            },
            "physical": {
                "title": "身体症状评估",
                "questions": [
                    "我感到疲劳或精力不足",
                    "我睡眠质量差",
                    "我有头痛或身体疼痛",
                    "我食欲发生变化",
                    "我经常生病"
                ]
            },
            "social": {
                "title": "社交关系评估",
                "questions": [
                    "我避免与同事交流",
                    "我不愿参加团队活动",
                    "我感到人际关系紧张",
                    "我难以表达自己的想法",
                    "我倾向于独自承担问题"
                ]
            }
        }
    
    def display_welcome(self):
        """显示欢迎信息"""
        print("=" * 60)
        print("🧘‍♂️ 程序员心理健康快速检测工具")
        print("=" * 60)
        print("这个工具将帮助您快速评估心理健康状态。")
        print("请根据最近两周的情况，诚实回答以下问题。")
        print("\n评分说明：")
        print("0 = 从不    1 = 偶尔    2 = 有时    3 = 经常    4 = 总是")
        print("=" * 60)
    
    def conduct_assessment(self) -> Dict:
        """进行心理健康评估"""
        results = {}
        total_score = 0
        max_score = 0
        
        for category, data in self.questions.items():
            print(f"\n📋 {data['title']}")
            print("-" * 40)
            
            category_score = 0
            for i, question in enumerate(data['questions'], 1):
                while True:
                    try:
                        score = int(input(f"{i}. {question} (0-4): "))
                        if 0 <= score <= 4:
                            category_score += score
                            break
                        else:
                            print("请输入0-4之间的数字")
                    except ValueError:
                        print("请输入有效的数字")
            
            results[category] = {
                "score": category_score,
                "max_score": len(data['questions']) * 4,
                "percentage": (category_score / (len(data['questions']) * 4)) * 100
            }
            
            total_score += category_score
            max_score += len(data['questions']) * 4
        
        results['total'] = {
            "score": total_score,
            "max_score": max_score,
            "percentage": (total_score / max_score) * 100
        }
        
        return results
    
    def interpret_results(self, results: Dict) -> Dict:
        """解释评估结果"""
        total_percentage = results['total']['percentage']
        
        # 总体评估
        if total_percentage <= 25:
            overall_level = "良好"
            overall_desc = "心理健康状态良好，继续保持！"
            overall_color = "🟢"
        elif total_percentage <= 50:
            overall_level = "一般"
            overall_desc = "需要关注某些方面，建议采取一些改进措施。"
            overall_color = "🟡"
        elif total_percentage <= 75:
            overall_level = "较差"
            overall_desc = "存在明显的心理健康问题，建议寻求专业帮助。"
            overall_color = "🟠"
        else:
            overall_level = "很差"
            overall_desc = "心理健康状况令人担忧，强烈建议立即咨询专业人士。"
            overall_color = "🔴"
        
        # 各维度评估
        category_interpretations = {}
        for category, data in results.items():
            if category == 'total':
                continue
                
            percentage = data['percentage']
            if percentage <= 25:
                level = "正常"
                color = "🟢"
            elif percentage <= 50:
                level = "轻度问题"
                color = "🟡"
            elif percentage <= 75:
                level = "中度问题"
                color = "🟠"
            else:
                level = "重度问题"
                color = "🔴"
            
            category_interpretations[category] = {
                "level": level,
                "color": color,
                "percentage": percentage
            }
        
        return {
            "overall": {
                "level": overall_level,
                "description": overall_desc,
                "color": overall_color,
                "percentage": total_percentage
            },
            "categories": category_interpretations
        }
    
    def display_results(self, results: Dict, interpretation: Dict):
        """显示评估结果"""
        print("\n" + "=" * 60)
        print("📊 评估结果")
        print("=" * 60)
        
        # 总体结果
        overall = interpretation['overall']
        print(f"\n{overall['color']} 总体评估: {overall['level']}")
        print(f"总分: {results['total']['score']}/{results['total']['max_score']} ({overall['percentage']:.1f}%)")
        print(f"说明: {overall['description']}")
        
        # 各维度结果
        print(f"\n📈 各维度详情:")
        print("-" * 40)
        
        category_names = {
            "stress": "压力水平",
            "mood": "情绪状态", 
            "cognitive": "认知功能",
            "physical": "身体症状",
            "social": "社交关系"
        }
        
        for category, interp in interpretation['categories'].items():
            name = category_names.get(category, category)
            score = results[category]['score']
            max_score = results[category]['max_score']
            print(f"{interp['color']} {name}: {score}/{max_score} ({interp['percentage']:.1f}%) - {interp['level']}")
    
    def provide_recommendations(self, interpretation: Dict):
        """提供改进建议"""
        print(f"\n💡 改进建议:")
        print("-" * 40)
        
        overall_percentage = interpretation['overall']['percentage']
        
        if overall_percentage <= 25:
            print("✅ 您的心理健康状态很好！建议：")
            print("   • 继续保持良好的工作生活平衡")
            print("   • 定期进行自我评估")
            print("   • 帮助其他同事维护心理健康")
        
        elif overall_percentage <= 50:
            print("⚠️ 需要适度关注，建议：")
            print("   • 学习压力管理技巧")
            print("   • 改善睡眠质量")
            print("   • 增加运动和放松活动")
            print("   • 寻求同事或朋友的支持")
        
        elif overall_percentage <= 75:
            print("🚨 建议采取积极行动：")
            print("   • 考虑寻求专业心理咨询")
            print("   • 调整工作强度和节奏")
            print("   • 学习情绪调节技巧")
            print("   • 建立更好的支持网络")
        
        else:
            print("🆘 强烈建议立即行动：")
            print("   • 立即寻求专业心理健康帮助")
            print("   • 考虑暂时减少工作压力")
            print("   • 告知信任的人您的状况")
            print("   • 关注自杀预防资源")
        
        # 针对性建议
        categories = interpretation['categories']
        high_risk_areas = [cat for cat, data in categories.items() if data['percentage'] > 50]
        
        if high_risk_areas:
            print(f"\n🎯 重点关注领域:")
            area_tips = {
                "stress": "压力管理：尝试深呼吸、冥想、时间管理技巧",
                "mood": "情绪调节：保持规律作息、适量运动、寻求社交支持",
                "cognitive": "认知功能：充足睡眠、减少多任务、定期休息",
                "physical": "身体健康：改善睡眠、健康饮食、定期体检",
                "social": "社交关系：主动沟通、参与团队活动、寻求帮助"
            }
            
            for area in high_risk_areas:
                if area in area_tips:
                    print(f"   • {area_tips[area]}")
    
    def save_results(self, results: Dict, interpretation: Dict):
        """保存评估结果"""
        timestamp = datetime.datetime.now().isoformat()
        
        data = {
            "timestamp": timestamp,
            "results": results,
            "interpretation": interpretation
        }
        
        # 读取历史记录
        history = []
        if os.path.exists(self.results_file):
            try:
                with open(self.results_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            except:
                history = []
        
        # 添加新记录
        history.append(data)
        
        # 保存到文件
        with open(self.results_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 结果已保存到 {self.results_file}")
    
    def show_trend(self):
        """显示历史趋势"""
        if not os.path.exists(self.results_file):
            print("暂无历史记录")
            return
        
        try:
            with open(self.results_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except:
            print("读取历史记录失败")
            return
        
        if len(history) < 2:
            print("需要至少2次评估才能显示趋势")
            return
        
        print("\n📈 历史趋势 (最近5次):")
        print("-" * 40)
        
        recent_history = history[-5:]
        for i, record in enumerate(recent_history):
            timestamp = record['timestamp'][:10]  # 只显示日期
            total_percentage = record['interpretation']['overall']['percentage']
            level = record['interpretation']['overall']['level']
            print(f"{i+1}. {timestamp}: {total_percentage:.1f}% ({level})")
    
    def run(self):
        """运行评估程序"""
        self.display_welcome()
        
        while True:
            print(f"\n请选择操作：")
            print("1. 开始心理健康评估")
            print("2. 查看历史趋势")
            print("3. 退出")
            
            choice = input("\n请输入选择 (1-3): ").strip()
            
            if choice == '1':
                results = self.conduct_assessment()
                interpretation = self.interpret_results(results)
                self.display_results(results, interpretation)
                self.provide_recommendations(interpretation)
                self.save_results(results, interpretation)
                
                print(f"\n🔗 更多资源:")
                print("   • 完整指南: https://github.com/yourusername/程序员修心指南")
                print("   • 专业帮助: 如需专业心理咨询，请联系当地心理健康机构")
                
            elif choice == '2':
                self.show_trend()
                
            elif choice == '3':
                print("\n感谢使用程序员心理健康检测工具！")
                print("记住：照顾好自己的心理健康，就像维护代码一样重要。💚")
                break
                
            else:
                print("无效选择，请重新输入")

def main():
    """主函数"""
    checker = MentalHealthChecker()
    checker.run()

if __name__ == "__main__":
    main()
