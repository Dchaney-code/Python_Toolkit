starting_coordinates = (100, 64, -50)
wall_coordinates ={
    (0, 0, 0): "minecraft:stone_bricks",
    (1, 0, 0): "minecraft:stone_bricks",
    (2, 0, 0): "minecraft:stone_bricks",
}

originX, originY, originZ = starting_coordinates

print("--- GOLEM CONSTRUCTION SCHEDULE ---")

for offset, block_name in wall_coordinates.items():
    dx, dy, dz = offset
    worldX = originX + dx
    worldY = originY + dy
    worldZ = originZ + dz

    processed_coordinates = (worldX, worldY, worldZ)

    print(f"Place {block_name} at {processed_coordinates}")