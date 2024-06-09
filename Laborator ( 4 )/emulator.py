
import random
def generate_random(cfg, symbol, depth=10):
    if depth == 0:
        return symbol if symbol in cfg['Sigma'] else ""

    if symbol in cfg['Sigma']:
        return symbol

    applicable_rules = [rule for rule in cfg['Rules'] if rule[0] == symbol]
    if not applicable_rules:
        return ""

    chosen_rule = random.choice(applicable_rules)
    return ''.join(generate_random(cfg, sym, depth - 1) for sym in chosen_rule[1])