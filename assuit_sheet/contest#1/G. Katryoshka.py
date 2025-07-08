eyes, mouth, body = map(int, input().split())
counter = 0

if eyes > 0 and mouth > 0 and body > 0:
    x = min(eyes, mouth, body)
    counter += x
    eyes -= x
    mouth -= x
    body -= x

if eyes == 0 or body == 0:
    counter += 0
else:
    x = eyes // 2
    counter += min(x, body)

print(counter)
