"""Este app ajuda a imprimir apenas os emails dos estudantes cadastrados formando uma lista.
Ele será útil para quando quisermos selecionar apenas um item de uma lista/dicionário."""

michaelsons = {
    "filhos":
    [
        {"name":"Elijah Mickaelson", "email":"elijah@exemplo.com"},
        {"name":"Klaus Mickaelson", "email":"klaus@exemplo.com"},
        {"name":"Finn Mickaelson", "email":"finn@exemplo.com" },
        {"name":"Kol Mickaelson", "email":"kol@exemplo.com" },
        {"name":"Freya Mickaelson", "email":"freya@exemplo.com" },
        {"name":"Rebekah Mickaelson", "email":"rebekah@exemplo.com" },
    ]
        }

for original in michaelsons ["filhos"]:
    print(original["email"])
