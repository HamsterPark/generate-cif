"""
generate_cif.py
从原子位置表生成 CIF 文件的通用脚本。
使用方法：直接运行即可生成 Al2(MoO4)3 的 CIF 文件。
也可以修改下方参数生成其他晶体的 CIF。
"""


def generate_cif(
    filename,
    formula,
    name,
    a, b, c,
    alpha, beta, gamma,
    space_group_name,
    space_group_number,
    symmetry_ops,
    atoms,
):
    """
    生成 CIF 文件。

    Parameters
    ----------
    filename : str
        输出文件名，如 'Al2Mo3O12.cif'
    formula : str
        化学式，如 'Al2 Mo3 O12'
    name : str
        化合物名称
    a, b, c : float
        晶格参数（单位：Å）
    alpha, beta, gamma : float
        晶格角度（单位：°）
    space_group_name : str
        空间群 Hermann-Mauguin 符号，如 'P 21/a'
    space_group_number : int
        空间群编号
    symmetry_ops : list of str
        对称操作列表
    atoms : list of dict
        原子列表，每个 dict 包含:
        label, symbol, x, y, z, occ, u_iso
    """
    lines = []
    lines.append(f"data_{formula.replace(' ', '')}")
    lines.append(f"_chemical_formula_sum            '{formula}'")
    lines.append(f"_chemical_name_common            '{name}'")
    lines.append("")
    lines.append(f"_cell_length_a                   {a:.4f}")
    lines.append(f"_cell_length_b                   {b:.4f}")
    lines.append(f"_cell_length_c                   {c:.4f}")
    lines.append(f"_cell_angle_alpha                {alpha:.2f}")
    lines.append(f"_cell_angle_beta                 {beta:.2f}")
    lines.append(f"_cell_angle_gamma                {gamma:.2f}")
    lines.append("")
    lines.append(f"_symmetry_space_group_name_H-M   '{space_group_name}'")
    lines.append(f"_symmetry_Int_Tables_number      {space_group_number}")
    lines.append("")

    # 对称操作
    lines.append("loop_")
    lines.append("_symmetry_equiv_pos_as_xyz")
    for op in symmetry_ops:
        lines.append(f"  '{op}'")
    lines.append("")

    # 原子坐标
    lines.append("loop_")
    lines.append("_atom_site_label")
    lines.append("_atom_site_type_symbol")
    lines.append("_atom_site_fract_x")
    lines.append("_atom_site_fract_y")
    lines.append("_atom_site_fract_z")
    lines.append("_atom_site_occupancy")
    lines.append("_atom_site_U_iso_or_equiv")
    for atom in atoms:
        lines.append(
            f"  {atom['label']:<6s}{atom['symbol']:<4s}"
            f"{atom['x']:>9.4f}{atom['y']:>9.4f}{atom['z']:>9.4f}"
            f"{atom['occ']:>6.1f}{atom['u_iso']:>10.4f}"
        )

    with open(filename, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"CIF 文件已生成：{filename}")


# ============================================================
# Al2(MoO4)3 的具体数据 —— 修改这里可生成其他晶体的 CIF
# ============================================================

atoms = [
    {"label": "Al1",  "symbol": "Al", "x":  0.3810, "y": 0.974, "z": 0.313,   "occ": 1.0, "u_iso":  0.0021},
    {"label": "Al2",  "symbol": "Al", "x":  0.3730, "y": 0.454, "z": 0.050,   "occ": 1.0, "u_iso":  0.0169},
    {"label": "Al3",  "symbol": "Al", "x":  0.1170, "y": 0.471, "z": 0.179,   "occ": 1.0, "u_iso":  0.0379},
    {"label": "Al4",  "symbol": "Al", "x":  0.1090, "y": 0.979, "z": 0.420,   "occ": 1.0, "u_iso":  0.0259},
    {"label": "Mo1",  "symbol": "Mo", "x": -0.0350, "y": 0.247, "z": 0.4888,  "occ": 1.0, "u_iso":  0.0111},
    {"label": "Mo2",  "symbol": "Mo", "x":  0.3580, "y": 0.122, "z": 0.1318,  "occ": 1.0, "u_iso":  0.0090},
    {"label": "Mo3",  "symbol": "Mo", "x":  0.1433, "y": 0.111, "z": 0.2563,  "occ": 1.0, "u_iso": -0.0057},
    {"label": "Mo4",  "symbol": "Mo", "x":  0.1470, "y": 0.618, "z": 0.3805,  "occ": 1.0, "u_iso":  0.0145},
    {"label": "Mo5",  "symbol": "Mo", "x":  0.3531, "y": 0.626, "z": 0.2194,  "occ": 1.0, "u_iso":  0.0404},
    {"label": "Mo6",  "symbol": "Mo", "x":  0.0026, "y": 0.745, "z": 0.018,   "occ": 1.0, "u_iso":  0.0168},
    {"label": "O1",   "symbol": "O",  "x":  0.5802, "y": 0.392, "z":-0.0095,  "occ": 1.0, "u_iso":  0.0021},
    {"label": "O2",   "symbol": "O",  "x":  0.9897, "y": 0.417, "z": 0.1676,  "occ": 1.0, "u_iso":  0.3347},
    {"label": "O3",   "symbol": "O",  "x":  0.8310, "y": 0.190, "z": 0.0958,  "occ": 1.0, "u_iso": -0.0250},
    {"label": "O4",   "symbol": "O",  "x":  0.7655, "y": 0.501, "z": 0.046,   "occ": 1.0, "u_iso":  0.2862},
    {"label": "O5",   "symbol": "O",  "x":  0.5200, "y": 0.431, "z": 0.1482,  "occ": 1.0, "u_iso": -0.0338},
    {"label": "O6",   "symbol": "O",  "x":  0.7358, "y": 0.515, "z": 0.2727,  "occ": 1.0, "u_iso": -0.0167},
    {"label": "O7",   "symbol": "O",  "x":  0.4176, "y": 0.115, "z": 0.4036,  "occ": 1.0, "u_iso": -0.0159},
    {"label": "O8",   "symbol": "O",  "x":  0.1798, "y": 0.292, "z": 0.2506,  "occ": 1.0, "u_iso": -0.0334},
    {"label": "O9",   "symbol": "O",  "x":  0.5554, "y": 0.361, "z": 0.4471,  "occ": 1.0, "u_iso":  0.2604},
    {"label": "O10",  "symbol": "O",  "x":  0.3909, "y": 0.320, "z": 0.9845,  "occ": 1.0, "u_iso":  0.0864},
    {"label": "O11",  "symbol": "O",  "x":  0.0715, "y": 0.372, "z": 0.0737,  "occ": 1.0, "u_iso":  0.6387},
    {"label": "O12",  "symbol": "O",  "x":  0.4116, "y": 0.358, "z": 0.502,   "occ": 1.0, "u_iso":  0.0096},
    {"label": "O13",  "symbol": "O",  "x":  0.8607, "y": 0.395, "z": 0.2314,  "occ": 1.0, "u_iso":  0.0814},
    {"label": "O14",  "symbol": "O",  "x":  0.2500, "y": 0.020, "z": 0.5183,  "occ": 1.0, "u_iso":  0.0943},
    {"label": "O15",  "symbol": "O",  "x":  0.1270, "y": 0.098, "z": 0.3445,  "occ": 1.0, "u_iso":  0.1140},
    {"label": "O16",  "symbol": "O",  "x":  0.5250, "y": 0.937, "z": 0.3562,  "occ": 1.0, "u_iso": -0.0224},
    {"label": "O17",  "symbol": "O",  "x":  0.7450, "y": 0.972, "z": 0.2013,  "occ": 1.0, "u_iso":  0.0116},
    {"label": "O18",  "symbol": "O",  "x":  0.6620, "y": 0.930, "z": 0.2946,  "occ": 1.0, "u_iso":  0.0314},
    {"label": "O19",  "symbol": "O",  "x":  0.9730, "y": 0.943, "z": 0.3225,  "occ": 1.0, "u_iso": -0.0056},
    {"label": "O20",  "symbol": "O",  "x":  0.0974, "y": 0.327, "z": 0.5927,  "occ": 1.0, "u_iso":  0.1053},
    {"label": "O21",  "symbol": "O",  "x":  0.1607, "y": 0.803, "z": 0.3970,  "occ": 1.0, "u_iso":  0.1413},
    {"label": "O22",  "symbol": "O",  "x":  0.0530, "y": 0.646, "z": 0.1197,  "occ": 1.0, "u_iso":  0.0772},
    {"label": "O23",  "symbol": "O",  "x":  0.3620, "y": 0.599, "z": 0.1236,  "occ": 1.0, "u_iso": -0.0131},
    {"label": "O24",  "symbol": "O",  "x":  0.3415, "y": 0.817, "z": 0.2307,  "occ": 1.0, "u_iso": -0.0437},
]

# P21/a 的对称操作
symmetry_ops = [
    "x, y, z",
    "-x+1/2, y+1/2, -z",
    "-x, -y, -z",
    "x+1/2, -y+1/2, z",
]

if __name__ == "__main__":
    generate_cif(
        filename="Al2Mo3O12.cif",
        formula="Al2 Mo3 O12",
        name="Aluminum Molybdate",
        a=15.49, b=9.11, c=18.00,
        alpha=90.00, beta=125.30, gamma=90.00,
        space_group_name="P 21/a",
        space_group_number=14,
        symmetry_ops=symmetry_ops,
        atoms=atoms,
    )
