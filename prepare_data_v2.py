# backend/prepare_data_v3.py

import os, shutil

RAW_ROOT   = 'data_raw'
OUT_BASE   = 'data'
CLASS_MAP  = {'No_Dr': 0, 'Dr': 1}
SUBSET_MAP = {
    'train': 'train',
    'valid': 'val',
    'validation': 'val'
}

# 1) Prépare l’arborescence de sortie
for subset_out in set(SUBSET_MAP.values()):
    for cls_idx in CLASS_MAP.values():
        os.makedirs(os.path.join(OUT_BASE, subset_out, str(cls_idx)), exist_ok=True)

# 2) Parcours récursif de data_raw
copied = {(s,c): 0 for s in SUBSET_MAP.values() for c in CLASS_MAP.values()}

for dirpath, dirnames, _ in os.walk(RAW_ROOT):
    base = os.path.basename(dirpath).lower()
    if base in SUBSET_MAP:
        subset_out = SUBSET_MAP[base]
        # On regarde les sous-dossiers à l’intérieur : Dr et No_Dr
        for cls_name, cls_idx in CLASS_MAP.items():
            src_cls = os.path.join(dirpath, cls_name)
            if not os.path.isdir(src_cls):
                continue
            dst_cls = os.path.join(OUT_BASE, subset_out, str(cls_idx))
            for fn in os.listdir(src_cls):
                src_f = os.path.join(src_cls, fn)
                dst_f = os.path.join(dst_cls, fn)
                if os.path.isfile(src_f) and not os.path.exists(dst_f):
                    shutil.copy2(src_f, dst_f)
                    copied[(subset_out, cls_idx)] += 1

# 3) Bilan
print("=== Bilan de la préparation v3 ===")
for (subset, cls), cnt in sorted(copied.items()):
    print(f"  {subset} / classe {cls} : {cnt} images copiées")
