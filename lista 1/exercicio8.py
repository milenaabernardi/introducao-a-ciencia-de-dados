def estatisticas(*args):
    return {
        "média": sum(args) / len(args),
        "máximo": max(args),
        "mínimo": min(args)
    }

print(estatisticas(10, 20, 30, 40, 50))