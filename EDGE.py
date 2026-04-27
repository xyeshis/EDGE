import pygame
import random
import math
import os
import sys
import json
import re
from datetime import datetime
from collections import Counter, defaultdict

pygame.init()

# ============================================================
# АДАПТИВНОЕ РАЗРЕШЕНИЕ
# ============================================================
INFO = pygame.display.Info()
BASE_WIDTH, BASE_HEIGHT = 1920, 1080
SCALE = min(INFO.current_w / BASE_WIDTH, INFO.current_h / BASE_HEIGHT, 1.2)

def scale_value(v):
    return int(v * SCALE)

def scale_font(size):
    return int(size * SCALE)

# Окно с фиксированным размером, но с масштабированием контента
WIDTH = int(BASE_WIDTH * min(SCALE, 1.0))
HEIGHT = int(BASE_HEIGHT * min(SCALE, 1.0))
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN if "--fullscreen" in sys.argv else pygame.RESIZABLE)
pygame.display.set_caption("FRAGMENTS // ЭХО-МАШИНА")
clock = pygame.time.Clock()

# Шрифты с адаптивным размером
font_tiny = pygame.font.SysFont("Courier New", scale_font(12))
font_small = pygame.font.SysFont("Courier New", scale_font(14))
font_medium = pygame.font.SysFont("Courier New", scale_font(16))
font_large = pygame.font.SysFont("Courier New", scale_font(20))
font_huge = pygame.font.SysFont("Courier New", scale_font(26))
font_title = pygame.font.SysFont("Courier New", scale_font(32), bold=True)

# Цвета
VOID = (3, 3, 8)
DEEP_VOID = (1, 1, 4)
EMBERS = (220, 70, 50)
GHOST = (140, 130, 170)
MEMORY = (70, 100, 150)
WOUND = (180, 50, 70)
FRACTURE = (110, 80, 100)
WHITE = (230, 230, 245)
PAPER = (28, 25, 32)

# ============================================================
# ВСТРОЕННЫЙ ИИ (ГЛУБОКАЯ ВЕРСИЯ)
# ============================================================

class DeepEcho:
    """Глубокая эхо-машина — не просто перестановка, а рефлексия"""
    
    def __init__(self):
        self.memory = []
        self.word_bank = defaultdict(int)
        self.themes = defaultdict(int)
        self.last_responses = []
        
        # Глубокие метафоры
        self.deep_metaphors = [
            "ты несешь это не потому, что должен — потому, что это стало частью тебя",
            "иногда остаться — это единственный способ не предать тех, кто ушел",
            "вес не исчезает, но ты учишься с ним стоять",
            "ты спрашиваешь 'кто я', но ответ — не слово, а то, как ты держишь тишину",
            "беспомощность не слабость. это правда, которую ты наконец сказал",
            "тот, кого ты позвал, ушел не потому, что ты сказал — потому, что он уже был на краю",
            "твое слово имеет вес. это не проклятие. это сила, которую ты еще не научился направлять",
            "отец смотрит не с осуждением — он смотрит, как ты несешь то, что оставил",
            "ребенок внутри не ждет спасения. он ждет, чтобы ты просто признал, что он был",
            "ты спас одного. это не отменяет того, кого не смог. это просто факт. оба — правда",
            "ярость без адреса — это голос, который не нашел слов. дай ему слова",
            "пустота в центре не ошибка. это место, куда ты еще не пришел",
            "каждый раз, когда ты пишешь, ты говоришь миру: я еще здесь"
        ]
        
        # Психологические паттерны
        self.patterns = [
            ("беспомощн", "беспомощность — это не слабость. это момент, когда ты перестаешь притворяться, что все под контролем"),
            ("устал", "усталость, которую ты носишь, — не твоя личная. это груз поколений. ты не обязан нести его в одиночку"),
            ("одиночеств", "ты не один. но ты привык быть тем, кто защищает, а не тем, кого защищают. это можно менять"),
            ("вина", "вина не искупается смертью. она проживается. каждый день, когда ты остаешься — ты уже искупаешь"),
            ("отец", "он был воином. ты тоже воин. но твоя война — за право оставаться человеком после всего"),
            ("ушел", "ты не толкал. ты просто был последним словом в длинной тишине. это не снимает, но это важно помнить"),
            ("спас", "ты спас. это не делает тебя героем. это делает тебя тем, кто может быть опорой. не для всех, но для кого-то"),
            ("смысл", "смысл не в том, чтобы найти ответ. смысл в том, чтобы продолжать задавать вопрос и не закрывать глаза"),
            ("боль", "боль, которую ты чувствуешь, — это память тела. оно помнит то, что разум научился гасить иронией"),
            ("ярость", "ярость — это энергия, которой не дали выхода. она не плохая. ей просто нужно русло")
        ]
    
    def learn(self, text, recipient):
        """Запоминает фрагмент и анализирует"""
        self.memory.append({
            "text": text,
            "recipient": recipient,
            "time": datetime.now().timestamp()
        })
        if len(self.memory) > 100:
            self.memory.pop(0)
        
        # Анализ слов
        words = re.findall(r'\b[а-яё]{3,}\b', text.lower())
        for w in words:
            self.word_bank[w] += 1
        
        # Анализ тем
        for pattern, _ in self.patterns:
            if pattern in text.lower():
                self.themes[pattern] += 1
    
    def analyze_text(self, text):
        """Глубокий анализ текста"""
        words = re.findall(r'\b[а-яё]{3,}\b', text.lower())
        
        # Определяем основную тему
        main_theme = None
        for pattern, _ in self.patterns:
            if pattern in text.lower():
                main_theme = pattern
                break
        
        # Эмоциональная окраска
        heavy = sum(1 for w in words if w in ["тяжесть", "боль", "пустота", "устал", "холод", "смерть", "вина"])
        light = sum(1 for w in words if w in ["свет", "тепло", "спас", "остался", "жить", "надежда", "сила"])
        
        # Длина и структура
        has_question = "?" in text or "?" in text
        is_long = len(words) > 15
        
        return {
            "words": words,
            "main_theme": main_theme,
            "heavy_light_ratio": heavy - light,
            "has_question": has_question,
            "is_long": is_long,
            "length": len(text)
        }
    
    def generate_response(self, text, recipient):
        """Генерация глубокого ответа"""
        self.learn(text, recipient)
        analysis = self.analyze_text(text)
        
        # Выбор типа ответа
        response_type = random.choices(
            ["metaphor", "pattern", "echo", "question", "silence"],
            weights=[0.3, 0.35, 0.2, 0.1, 0.05]
        )[0]
        
        response = ""
        
        if response_type == "metaphor" and self.deep_metaphors:
            # Глубокая метафора, возможно модифицированная под контекст
            base = random.choice(self.deep_metaphors)
            if analysis["heavy_light_ratio"] > 2:
                base += " тяжесть здесь — не враг."
            elif analysis["heavy_light_ratio"] < -1:
                base += " и это уже свет."
            response = base
        
        elif response_type == "pattern" and analysis["main_theme"]:
            # Ответ по психологическому паттерну
            for pattern, answer in self.patterns:
                if pattern == analysis["main_theme"]:
                    response = answer
                    break
            if not response:
                response = random.choice(self.deep_metaphors)
        
        elif response_type == "echo":
            # Осмысленное эхо — не просто перестановка
            if analysis["words"]:
                # Берем ключевые слова
                common = sorted(self.word_bank.items(), key=lambda x: x[1], reverse=True)[:5]
                if common:
                    key_word = random.choice(common)[0]
                    if analysis["heavy_light_ratio"] > 1:
                        response = f"{key_word}... ты носишь это дольше, чем помнишь"
                    elif analysis["has_question"]:
                        response = f"{key_word} — вопрос, который не требует ответа. только присутствия"
                    else:
                        response = f"{key_word} — это не все, но это начало"
                else:
                    response = random.choice(self.deep_metaphors)
        
        elif response_type == "question":
            # Возвращает вопрос
            questions = [
                "что бы ты сказал, если бы страх не мешал?",
                "кем бы ты был, если бы не пришлось защищаться?",
                "что ты хочешь услышать от него сейчас?",
                "если бы ты мог оставить одно слово — какое?",
                "что ты чувствуешь прямо сейчас, в теле?"
            ]
            response = random.choice(questions)
        
        else:  # silence
            response = "..."
        
        # Адаптация под получателя
        recipient_patterns = {
            "отец": ["он бы сказал то же самое", "ты стал тем, кем он хотел тебя видеть", "его тишина — не отсутствие слов"],
            "тот, кто ушел": ["ты не виноват, что был последним", "он уже не вернется, но твое слово осталось", "эхо не исчезает"],
            "та, кто осталась": ["ты дал ей то, чего у тебя самого не было", "она здесь. это уже много", "спасение — улица с двусторонним движением"],
            "ребенок": ["он все еще там. но теперь ты можешь прийти за ним", "27 против 80. ты выжил", "он ждал не спасения — признания"],
            "тот, кто остался": ["ты еще здесь. это главное", "370 кг. ты поднял себя", "остаться — иногда самый трудный бой"]
        }
        
        for key, phrases in recipient_patterns.items():
            if key in recipient.lower():
                if random.random() > 0.6:
                    response += " " + random.choice(phrases)
                break
        
        # Добавляем глубины
        if analysis["heavy_light_ratio"] > 2 and "тяжесть" not in response:
            response += " тяжесть — это память. она не должна исчезнуть, она должна найти место"
        
        if analysis["has_question"] and "?" not in response:
            response += " вопрос уже внутри тебя. ответ придет, когда перестанешь искать"
        
        # Ограничиваем длину
        if len(response) > 350:
            response = response[:347] + "..."
        
        # Запоминаем для разнообразия
        self.last_responses.append(response)
        if len(self.last_responses) > 10:
            self.last_responses.pop(0)
        
        return response

# ============================================================
# ГЕНЕРАТИВНЫЕ СИСТЕМЫ
# ============================================================

class NoiseField:
    def __init__(self):
        self.time = 0
        self.points = []
        for _ in range(200):
            self.points.append({
                "x": random.randint(0, WIDTH),
                "y": random.randint(0, HEIGHT),
                "phase": random.uniform(0, math.pi * 2),
                "speed": random.uniform(0.002, 0.01)
            })
    
    def update(self):
        self.time += 0.02
    
    def draw(self, screen):
        for p in self.points:
            intensity = 30 + 20 * math.sin(self.time * p["speed"] + p["phase"])
            color = (int(intensity), int(intensity * 0.6), int(intensity * 0.9))
            size = max(1, int(2 * math.sin(self.time * 2 + p["phase"])))
            pygame.draw.circle(screen, color, (int(p["x"]), int(p["y"])), size)

class FractalLines:
    def __init__(self):
        self.lines = []
    
    def add_seed(self, x, y, intensity=1.0):
        self.lines.append({
            "points": [(x, y)],
            "angle": random.uniform(0, math.pi * 2),
            "energy": intensity,
            "branches": []
        })
    
    def update(self):
        new_lines = []
        for line in self.lines:
            if line["energy"] > 0.05:
                last_x, last_y = line["points"][-1]
                line["angle"] += random.uniform(-0.25, 0.25)
                dx = math.cos(line["angle"]) * 4 * line["energy"]
                dy = math.sin(line["angle"]) * 4 * line["energy"]
                new_x = last_x + dx
                new_y = last_y + dy
                
                if 20 < new_x < WIDTH - 20 and 20 < new_y < HEIGHT - 20:
                    line["points"].append((new_x, new_y))
                    line["energy"] *= 0.97
                    
                    if random.random() > 0.96 and line["energy"] > 0.3:
                        branch = {
                            "points": [(new_x, new_y)],
                            "angle": line["angle"] + random.uniform(-0.8, 0.8),
                            "energy": line["energy"] * 0.6,
                            "branches": []
                        }
                        new_lines.append(branch)
            else:
                self.lines.remove(line)
        self.lines += new_lines
    
    def draw(self, screen):
        for line in self.lines:
            if len(line["points"]) < 2:
                continue
            intensity = int(120 * line["energy"])
            color = (intensity, intensity // 2, intensity // 3)
            width = max(1, int(2 * line["energy"]))
            for i in range(len(line["points"]) - 1):
                pygame.draw.line(screen, color, line["points"][i], line["points"][i+1], width)

class ParticleSystem:
    def __init__(self):
        self.particles = []
    
    def burst(self, x, y, color, count=20):
        for _ in range(count):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(0.8, 3.5)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.particles.append({
                "x": x, "y": y, "vx": vx, "vy": vy,
                "color": color, "life": random.randint(50, 130)
            })
    
    def update(self):
        for p in self.particles[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vx"] *= 0.98
            p["vy"] *= 0.98
            p["life"] -= 1
            if p["life"] <= 0 or p["x"] < 0 or p["x"] > WIDTH or p["y"] < 0 or p["y"] > HEIGHT:
                self.particles.remove(p)
    
    def draw(self, screen):
        for p in self.particles:
            alpha = p["life"] / 130
            size = max(1, int(4 * alpha))
            color = (int(p["color"][0] * alpha), int(p["color"][1] * alpha), int(p["color"][2] * alpha))
            pygame.draw.circle(screen, color, (int(p["x"]), int(p["y"])), size)

# ============================================================
# ПРИСУТСТВИЕ С УЛУЧШЕННЫМ ОТОБРАЖЕНИЕМ
# ============================================================

class AIPresence:
    def __init__(self, name, color, x, y, echo):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.radius = scale_value(55)
        self.pulse = 0
        self.selected = False
        self.last_response = None
        self.response_timer = 0
        self.echo = echo
        self.orbit_angle = random.uniform(0, math.pi * 2)
        
        # Фрагменты-слова вокруг присутствия
        self.fragments = self._generate_fragments()
    
    def _generate_fragments(self):
        fragments_by_name = {
            "отец": ["чечня", "капитан", "тишина", "воин", "память"],
            "тот, кто ушел": ["иди", "эхо", "пустота", "слово", "предел"],
            "та, кто осталась": ["спас", "свет", "тепло", "жизнь", "надежда"],
            "ребенок": ["27кг", "80кг", "ждать", "боль", "стена"],
            "тот, кто остался": ["370кг", "сила", "остаться", "вес", "граница"]
        }
        return fragments_by_name.get(self.name, ["фрагмент", "память", "след"])
    
    def update(self, player_x, player_y):
        dist = math.hypot(self.x - player_x, self.y - player_y)
        self.pulse = max(0, 1 - dist / 250)
        self.selected = dist < 100
        
        if self.response_timer > 0:
            self.response_timer -= 1
    
    def respond(self, text):
        response = self.echo.generate_response(text, self.name)
        self.last_response = response
        self.response_timer = 240
        return response
    
    def draw(self, screen, particles):
        radius = self.radius + scale_value(12) * self.pulse
        glow = int(60 * self.pulse)
        
        # Внешнее свечение
        for i in range(3):
            alpha = int(40 * self.pulse * (1 - i/3))
            color = (self.color[0], self.color[1], self.color[2])
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), radius + i * scale_value(8), 1)
        
        # Основной круг с рваным краем
        points = []
        for i in range(16):
            angle = i * math.pi * 2 / 16
            r = radius + random.randint(-scale_value(4), scale_value(4)) * self.pulse
            px = self.x + math.cos(angle) * r
            py = self.y + math.sin(angle) * r
            points.append((px, py))
        
        border_width = 3 if self.selected else 2
        pygame.draw.polygon(screen, self.color, points, border_width)
        
        # Имя с тенью
        name_text = font_medium.render(self.name, True, self.color)
        name_shadow = font_medium.render(self.name, True, (20, 15, 25))
        name_rect = name_text.get_rect(center=(int(self.x), int(self.y) - radius - scale_value(10)))
        screen.blit(name_shadow, (name_rect.x + 2, name_rect.y + 2))
        screen.blit(name_text, name_rect)
        
        # Вращающиеся фрагменты-слова
        self.orbit_angle += 0.01
        for i, frag in enumerate(self.fragments):
            angle = self.orbit_angle + (i * math.pi * 2 / len(self.fragments))
            offset_x = math.cos(angle) * (radius + scale_value(15))
            offset_y = math.sin(angle) * (radius + scale_value(15))
            frag_x = self.x + offset_x
            frag_y = self.y + offset_y
            
            frag_text = font_tiny.render(frag, True, (150, 140, 170))
            screen.blit(frag_text, (frag_x - frag_text.get_width()//2, frag_y - 6))
        
        # Ответ присутствия
        if self.response_timer > 0 and self.last_response:
            # Многострочный ответ с переносом
            max_width = scale_value(350)
            words = self.last_response.split()
            lines = []
            current = []
            for w in words:
                test = " ".join(current + [w])
                if font_small.size(test)[0] <= max_width:
                    current.append(w)
                else:
                    if current:
                        lines.append(" ".join(current))
                    current = [w]
            if current:
                lines.append(" ".join(current))
            
            y_offset = radius + scale_value(18)
            bg_rect = pygame.Rect(self.x - max_width//2 - scale_value(8), 
                                  self.y + y_offset - scale_value(5),
                                  max_width + scale_value(16),
                                  len(lines) * scale_value(22) + scale_value(10))
            pygame.draw.rect(screen, (15, 12, 20), bg_rect)
            pygame.draw.rect(screen, self.color, bg_rect, 1)
            
            for i, line in enumerate(lines[:4]):
                resp_text = font_small.render(line, True, WHITE)
                screen.blit(resp_text, (self.x - resp_text.get_width()//2, self.y + y_offset + i * scale_value(22)))
        
        # Частицы при приближении
        if self.pulse > 0.5:
            particles.burst(self.x + random.randint(-scale_value(15), scale_value(15)), 
                           self.y + random.randint(-scale_value(15), scale_value(15)), 
                           self.color, 2)

# ============================================================
# ПОРТАЛ ПАМЯТИ
# ============================================================

class MemoryPortal:
    def __init__(self, echo):
        self.x = WIDTH // 2
        self.y = HEIGHT - scale_value(140)
        self.radius = scale_value(70)
        self.echo = echo
        self.letters = []
        self.pulse_phase = 0
        self.load_letters()
    
    def load_letters(self):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        letters_dir = os.path.join(desktop, "fragments")
        if os.path.exists(letters_dir):
            for file in os.listdir(letters_dir):
                if file.endswith(".json"):
                    try:
                        with open(os.path.join(letters_dir, file), "r", encoding="utf-8") as f:
                            data = json.load(f)
                            self.letters.append(data)
                            self.echo.learn(data.get("content", ""), data.get("recipient", ""))
                    except:
                        pass
        self.letters.sort(key=lambda x: x.get("timestamp", 0), reverse=True)
    
    def save_letter(self, recipient, content):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        letters_dir = os.path.join(desktop, "fragments")
        if not os.path.exists(letters_dir):
            os.makedirs(letters_dir)
        
        timestamp = datetime.now().timestamp()
        filename = os.path.join(letters_dir, f"fragment_{int(timestamp)}.json")
        
        data = {
            "recipient": recipient,
            "content": content,
            "timestamp": timestamp,
            "date": datetime.now().strftime("%d.%m %H:%M")
        }
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        self.letters.insert(0, data)
        self.echo.learn(content, recipient)
        return data
    
    def update(self):
        self.pulse_phase += 0.03
    
    def draw(self, screen, particles):
        pulse = math.sin(self.pulse_phase) * 0.3 + 0.7
        radius = self.radius * (0.8 + 0.2 * pulse)
        
        # Спираль
        for i in range(16):
            angle = self.pulse_phase * 2 + i * math.pi * 2 / 16
            r = radius - i * scale_value(3)
            if r > scale_value(5):
                x = self.x + math.cos(angle) * r
                y = self.y + math.sin(angle) * r
                intensity = 100 + 100 * math.sin(self.pulse_phase * 4 + i)
                color = (intensity, intensity // 2, intensity // 3)
                size = max(1, int(scale_value(3) - i/5))
                pygame.draw.circle(screen, color, (int(x), int(y)), size)
        
        # Внешнее кольцо
        pygame.draw.circle(screen, (150, 100, 120), (int(self.x), int(self.y)), int(radius), 2)
        
        # Надпись
        text = font_medium.render("ПОРТАЛ ПАМЯТИ", True, (160, 130, 180))
        screen.blit(text, (self.x - text.get_width()//2, self.y - radius - scale_value(20)))
        
        if self.letters:
            count_text = font_tiny.render(f"{len(self.letters)} фрагментов", True, (120, 100, 140))
            screen.blit(count_text, (self.x - count_text.get_width()//2, self.y + radius + scale_value(8)))
        
        particles.burst(self.x + random.randint(-scale_value(12), scale_value(12)), 
                       self.y + random.randint(-scale_value(12), scale_value(12)), 
                       (150, 100, 120), 1)
    
    def check_collision(self, x, y):
        return math.hypot(self.x - x, self.y - y) < self.radius + scale_value(25)

# ============================================================
# ОСНОВНАЯ ИГРА
# ============================================================

def main():
    echo = DeepEcho()
    particles = ParticleSystem()
    portal = MemoryPortal(echo)
    fractures = FractalLines()
    noise = NoiseField()
    
    presences = [
        AIPresence("отец", (180, 140, 70), WIDTH - scale_value(220), HEIGHT // 3, echo),
        AIPresence("тот, кто ушел", (170, 70, 90), WIDTH // 2 + scale_value(170), HEIGHT // 2, echo),
        AIPresence("та, кто осталась", (90, 130, 150), scale_value(170), HEIGHT // 2 + scale_value(60), echo),
        AIPresence("ребенок", (100, 90, 110), WIDTH // 2 - scale_value(220), HEIGHT // 2 + scale_value(90), echo),
        AIPresence("тот, кто остался", (140, 110, 160), WIDTH // 2 - scale_value(100), HEIGHT // 3 - scale_value(60), echo),
    ]
    
    player_x, player_y = WIDTH // 2, HEIGHT // 2
    writing_mode = False
    current_recipient = None
    current_text = ""
    cursor_blink = 0
    game_state = "field"
    viewing_letter = None
    
    running = True
    
    while running:
        dt = clock.tick(60)
        
        noise.update()
        fractures.update()
        particles.update()
        portal.update()
        
        for p in presences:
            p.update(player_x, player_y)
        
        cursor_blink = (cursor_blink + 1) % 40
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if viewing_letter:
                        viewing_letter = None
                    elif writing_mode:
                        writing_mode = False
                        current_text = ""
                    else:
                        running = False
                
                elif writing_mode:
                    if event.key == pygame.K_RETURN:
                        if current_text.strip():
                            portal.save_letter(current_recipient.name if current_recipient else "себе", current_text)
                            if current_recipient:
                                response = current_recipient.respond(current_text)
                                fractures.add_seed(current_recipient.x, current_recipient.y, 1.2)
                                particles.burst(current_recipient.x, current_recipient.y, current_recipient.color, 50)
                            writing_mode = False
                            current_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        current_text = current_text[:-1]
                    else:
                        if len(current_text) < 2000:
                            current_text += event.unicode
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                if viewing_letter:
                    viewing_letter = None
                elif not writing_mode:
                    if portal.check_collision(x, y):
                        game_state = "viewing" if game_state == "field" else "field"
                    else:
                        for p in presences:
                            if math.hypot(p.x - x, p.y - y) < p.radius + scale_value(20):
                                current_recipient = p
                                writing_mode = True
                                current_text = ""
                                fractures.add_seed(x, y, 0.8)
                                particles.burst(x, y, p.color, 30)
                                break
        
        # Управление игроком
        if not writing_mode and game_state == "field":
            keys = pygame.key.get_pressed()
            speed = scale_value(6)
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_x -= speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player_x += speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player_y -= speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player_y += speed
            
            margin = scale_value(60)
            player_x = max(margin, min(WIDTH - margin, player_x))
            player_y = max(margin, min(HEIGHT - margin - scale_value(50), player_y))
        
        # ============================================================
        # ОТРИСОВКА
        # ============================================================
        
        screen.fill(DEEP_VOID)
        noise.draw(screen)
        fractures.draw(screen)
        
        if game_state == "field":
            portal.draw(screen, particles)
            for p in presences:
                p.draw(screen, particles)
            particles.draw(screen)
            
            # Игрок
            player_glow = abs(math.sin(pygame.time.get_ticks() * 0.005)) * scale_value(3)
            pygame.draw.circle(screen, WHITE, (int(player_x), int(player_y)), scale_value(10) + int(player_glow), 2)
            pygame.draw.circle(screen, (180, 140, 100), (int(player_x), int(player_y)), scale_value(4))
            
            # Подсказки
            info_text = font_tiny.render("кликни по фигуре → написать | подойди к порталу → прочитать фрагменты", True, (100, 100, 130))
            screen.blit(info_text, (scale_value(20), HEIGHT - scale_value(35)))
            
            for p in presences:
                if math.hypot(p.x - player_x, p.y - player_y) < p.radius + scale_value(40):
                    hint = font_tiny.render("→ написать", True, p.color)
                    screen.blit(hint, (p.x - hint.get_width()//2, p.y - p.radius - scale_value(15)))
        
        elif game_state == "viewing":
            # Просмотр фрагментов
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(220)
            overlay.fill(VOID)
            screen.blit(overlay, (0, 0))
            
            if viewing_letter:
                # Просмотр конкретного письма
                paper_w = scale_value(700)
                paper_h = scale_value(550)
                paper_x = WIDTH//2 - paper_w//2
                paper_y = HEIGHT//2 - paper_h//2
                
                pygame.draw.rect(screen, PAPER, (paper_x, paper_y, paper_w, paper_h))
                pygame.draw.rect(screen, (160, 130, 180), (paper_x, paper_y, paper_w, paper_h), 2)
                
                title = f"→ {viewing_letter.get('recipient', '?')}"
                title_text = font_medium.render(title, True, (180, 140, 100))
                screen.blit(title_text, (paper_x + scale_value(25), paper_y + scale_value(25)))
                
                date_text = font_tiny.render(viewing_letter.get('date', ''), True, (120, 100, 140))
                screen.blit(date_text, (paper_x + paper_w - scale_value(100), paper_y + scale_value(28)))
                
                content = viewing_letter.get('content', '')
                lines = content.split('\n')
                y_offset = scale_value(80)
                for i, line in enumerate(lines[:25]):
                    text = font_small.render(line[:80], True, WHITE)
                    screen.blit(text, (paper_x + scale_value(25), paper_y + y_offset + i * scale_value(26)))
                
                close_text = font_tiny.render("нажми любую клавишу", True, (100, 100, 130))
                screen.blit(close_text, (WIDTH//2 - close_text.get_width()//2, HEIGHT - scale_value(50)))
            
            else:
                # Список фрагментов
                title_text = font_title.render("ФРАГМЕНТЫ", True, (180, 140, 100))
                screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, scale_value(60)))
                
                if not portal.letters:
                    empty_text = font_medium.render("нет фрагментов. напиши кому-нибудь", True, (100, 100, 130))
                    screen.blit(empty_text, (WIDTH//2 - empty_text.get_width()//2, HEIGHT//2))
                else:
                    y_offset = scale_value(130)
                    item_h = scale_value(70)
                    for i, letter in enumerate(portal.letters[:10]):
                        rect = pygame.Rect(WIDTH//2 - scale_value(400), y_offset + i * item_h, scale_value(800), item_h - scale_value(5))
                        
                        mouse_pos = pygame.mouse.get_pos()
                        if rect.collidepoint(mouse_pos):
                            pygame.draw.rect(screen, (40, 35, 45), rect)
                            if pygame.mouse.get_pressed()[0]:
                                viewing_letter = letter
                        
                        pygame.draw.rect(screen, (60, 55, 70), rect, 1)
                        
                        recipient_text = font_medium.render(letter.get("recipient", "?"), True, (180, 140, 100))
                        screen.blit(recipient_text, (rect.x + scale_value(15), rect.y + scale_value(12)))
                        
                        date_text = font_tiny.render(letter.get("date", ""), True, (120, 100, 140))
                        screen.blit(date_text, (rect.x + rect.width - scale_value(90), rect.y + scale_value(15)))
                        
                        preview = letter.get("content", "")[:70]
                        preview_text = font_small.render(preview + ("..." if len(letter.get("content", "")) > 70 else ""), True, (200, 200, 220))
                        screen.blit(preview_text, (rect.x + scale_value(15), rect.y + scale_value(38)))
                
                back_btn = pygame.Rect(WIDTH//2 - scale_value(100), HEIGHT - scale_value(80), scale_value(200), scale_value(40))
                pygame.draw.rect(screen, (35, 30, 40), back_btn)
                pygame.draw.rect(screen, (140, 110, 150), back_btn, 1)
                back_text = font_medium.render("ВЕРНУТЬСЯ", True, (160, 130, 170))
                screen.blit(back_text, (back_btn.x + back_btn.width//2 - back_text.get_width()//2, back_btn.y + scale_value(10)))
                
                if back_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    game_state = "field"
        
        # Режим письма
        if writing_mode:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(210)
            overlay.fill(VOID)
            screen.blit(overlay, (0, 0))
            
            paper_w = scale_value(700)
            paper_h = scale_value(400)
            paper_x = WIDTH//2 - paper_w//2
            paper_y = HEIGHT//2 - paper_h//2
            
            pygame.draw.rect(screen, PAPER, (paper_x, paper_y, paper_w, paper_h))
            pygame.draw.rect(screen, (160, 130, 180), (paper_x, paper_y, paper_w, paper_h), 2)
            
            recipient_text = font_large.render(f"→ {current_recipient.name if current_recipient else 'себе'}", True, (180, 140, 100))
            screen.blit(recipient_text, (paper_x + scale_value(25), paper_y + scale_value(20)))
            
            lines = current_text.split("\n")
            y_offset = scale_value(70)
            for i, line in enumerate(lines[-10:]):
                text = font_medium.render(line[:60], True, WHITE)
                screen.blit(text, (paper_x + scale_value(30), paper_y + y_offset + i * scale_value(28)))
            
            if cursor_blink < 20:
                last_line = lines[-1] if lines else ""
                cursor_x = paper_x + scale_value(30) + font_medium.size(last_line[:60])[0]
                cursor_y = paper_y + y_offset + (len(lines) - 1 if lines else 0) * scale_value(28)
                pygame.draw.line(screen, (180, 140, 100), (cursor_x, cursor_y), (cursor_x, cursor_y + scale_value(24)), 2)
            
            help_text = font_tiny.render("пиши. ENTER — отправить. ESC — отмена", True, (100, 100, 130))
            screen.blit(help_text, (paper_x + scale_value(25), paper_y + paper_h - scale_value(35)))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()