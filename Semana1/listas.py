# frutas = ['Bananas', 'Manzanas', 'Kiwi']

# frutas.append("Piña")
# frutas.append("Piña")
# frutas.append("Piña")
# frutas.append("Piña")
# frutas.append("Piña")

# frutas.insert(0, "Mango")

# frutas.extend(['Fresas', 'Sandias'])

# print(frutas)

frutas = ['Mango', 'Bananas', 'Manzanas', 'Kiwi', 'Piña', 'Piña', 'Piña', 'Piña', 'Fresas', 'Sandias']

se_imprimio_piña = False

for fruta in frutas:
    if fruta == "Piña" and not se_imprimio_piña:
        se_imprimio_piña = True
    elif fruta == "Piña" and se_imprimio_piña:
        continue
    print(f"Me fascina {fruta}")
    
print(frutas)


