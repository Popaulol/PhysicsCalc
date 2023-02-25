import fractions
import tkinter as tk
from tkinter import ttk

num_typ = float


class NotEnoughData(Exception):
    pass


def construct(tab_control):
    glob_ma, glob_va, glob_mb, glob_vb, glob_mab, glob_vab = (
        None,
        None,
        None,
        None,
        None,
        None,
    )
    getting_ma, getting_va, getting_mb, getting_vb, getting_mab, getting_vab = (
        False,
        False,
        False,
        False,
        False,
        False,
    )

    def get_ma():
        nonlocal getting_ma, glob_ma
        if getting_ma:
            return None
        getting_ma = True
        if glob_ma is not None:
            getting_ma = False
            return glob_ma

        try:
            glob_ma = num_typ(ma_input.get())
        except ValueError:
            pass
        else:
            getting_ma = False
            return glob_ma

        if (mb := get_mb()) is not None and (mab := get_mab()) is not None:
            glob_ma = mab - mb
            getting_ma = False
            return glob_ma

        if (
                (mb := get_mb()) is not None
                and (va := get_va()) is not None
                and (vb := get_vb()) is not None
                and (vab := get_vab()) is not None
        ):
            glob_ma = mb * ((vab - vb) / (va - vab))
            getting_ma = False
            return glob_ma

        return None

    def get_mb():
        nonlocal getting_mb, glob_mb
        if getting_mb:
            return None
        getting_mb = True
        if glob_mb is not None:
            getting_mb = False
            return glob_mb

        try:
            glob_mb = num_typ(mb_input.get())
        except ValueError:
            pass
        else:
            getting_mb = False
            return glob_mb

        if (ma := get_ma()) is not None and (mab := get_mab()) is not None:
            glob_mb = mab - ma
            getting_mb = False
            return glob_mb

        if (
                (ma := get_ma()) is not None
                and (va := get_va()) is not None
                and (vb := get_vb()) is not None
                and (vab := get_vab()) is not None
        ):
            glob_mb = ma * ((vab - va) / (vb - vab))
            getting_mb = False
            return glob_mb

        return None

    def get_mab():
        nonlocal getting_mab, glob_mab
        if getting_mab:
            return None

        getting_mab = True
        if glob_mab is not None:
            return glob_mab

        try:
            glob_mab = num_typ(mab_input.get())
        except ValueError:
            pass
        else:
            getting_mab = False
            return glob_mab

        if (ma := get_ma()) is not None and (mb := get_mb()) is not None:
            glob_mab = ma + mb
            getting_mab = False
            return glob_mab

        return None

    def get_va():
        nonlocal getting_va, glob_va
        if getting_va:
            return None

        getting_va = True
        if glob_va is not None:
            return glob_va

        try:
            glob_va = num_typ(va_input.get())
        except ValueError:
            pass
        else:
            getting_va = False
            return glob_va

        if (
            (mab := get_mab()) is not None
            and (ma := get_ma()) is not None
            and (mb := get_mb()) is not None
            and (vb := get_vb()) is not None
            and (vab := get_vab()) is not None
        ):
            glob_va = (mab * vab - mb * vb) / ma
            getting_va = False
            return glob_va

        return None


    def get_vb():
        nonlocal getting_vb, glob_vb
        if getting_vb:
            return None

        getting_vb = True
        if glob_vb is not None:
            return glob_vb

        try:
            glob_vb = num_typ(vb_input.get())
        except ValueError:
            pass
        else:
            getting_vb = False
            return glob_vb

        if (
                (mab := get_mab()) is not None
                and (ma := get_ma()) is not None
                and (mb := get_mb()) is not None
                and (va := get_va()) is not None
                and (vab := get_vab()) is not None
        ):
            glob_vb = (mab * vab - ma * va) / mb
            getting_vb = False
            return glob_vb

        return None

    def get_vab():
        nonlocal getting_vab, glob_vab
        if getting_vab:
            return None

        getting_vab = True
        if glob_vab is not None:
            return glob_vab

        try:
            glob_vab = num_typ(vab_input.get())
        except ValueError:
            pass
        else:
            getting_vab = False
            return glob_vab

        if (
                (mab := get_mab()) is not None
                and (ma := get_ma()) is not None
                and (mb := get_mb()) is not None
                and (va := get_va()) is not None
                and (vb := get_vb()) is not None
        ):
            glob_vab = (ma * va + mb * vb) / mab


        return None

    def refresh_screen():
        nonlocal glob_ma, glob_va, glob_mb, glob_vb, glob_mab, glob_vab
        nonlocal getting_ma, getting_va, getting_mb, getting_vb, getting_mab, getting_vab
        glob_ma, glob_va, glob_mb, glob_vb, glob_mab, glob_vab = (
            None,
            None,
            None,
            None,
            None,
            None,
        )
        getting_ma, getting_va, getting_mb, getting_vb, getting_mab, getting_vab = (
            False,
            False,
            False,
            False,
            False,
            False,
        )

        ma_out.config(text=str(get_ma()))

        va_out.config(text=str(get_va()))
        mb_out.config(text=str(get_mb()))
        vb_out.config(text=str(get_vb()))
        mab_out.config(text=str(get_mab()))
        vab_out.config(text=str(get_vab()))

    ma_input = tk.StringVar()
    va_input = tk.StringVar()

    mb_input = tk.StringVar()
    vb_input = tk.StringVar()

    mab_input = tk.StringVar()
    vab_input = tk.StringVar()

    frame = ttk.Frame(tab_control)
    ttk.Label(frame, text="Rechner für den Elastischen Stoß").grid(
        column=0, row=0, columnspan=10
    )

    ttk.Label(frame, text="Ma  =").grid(column=0, row=1)
    ttk.Entry(frame, width=5, textvariable=ma_input).grid(column=1, row=1)
    ttk.Label(frame, text="Va  =").grid(column=2, row=1)
    ttk.Entry(frame, width=5, textvariable=va_input).grid(column=3, row=1)

    ttk.Label(frame, text="Mb  =").grid(column=0, row=2)
    ttk.Entry(frame, width=5, textvariable=mb_input).grid(column=1, row=2)
    ttk.Label(frame, text="Vb  =").grid(column=2, row=2)
    ttk.Entry(frame, width=5, textvariable=vb_input).grid(column=3, row=2)

    ttk.Label(frame, text="Mab  =").grid(column=0, row=3)
    ttk.Entry(frame, width=5, textvariable=mab_input).grid(column=1, row=3)
    ttk.Label(frame, text="Vab  =").grid(column=2, row=3)
    ttk.Entry(frame, width=5, textvariable=vab_input).grid(column=3, row=3)

    ttk.Button(frame, text="Calculate Missing Values", command=refresh_screen).grid(
        column=0, row=4, columnspan=4
    )

    ttk.Label(frame).grid(column=0, row=5)

    ttk.Label(frame, text="Ma  =").grid(column=0, row=6)
    ma_out = ttk.Label(frame)
    ma_out.grid(column=1, row=6)
    ttk.Label(frame, text="Va  =").grid(column=2, row=6)
    va_out = ttk.Label(frame)
    va_out.grid(column=1, row=6)

    ttk.Label(frame, text="Mb  =").grid(column=0, row=7)
    mb_out = ttk.Label(frame)
    mb_out.grid(column=1, row=7)
    ttk.Label(frame, text="Vb  =").grid(column=2, row=7)
    vb_out = ttk.Label(frame)
    vb_out.grid(column=1, row=7)

    ttk.Label(frame, text="Mab  =").grid(column=0, row=8)
    mab_out = ttk.Label(frame)
    mab_out.grid(column=1, row=8)
    ttk.Label(frame, text="Vab  =").grid(column=2, row=8)
    vab_out = ttk.Label(frame)
    vab_out.grid(column=1, row=8)

    return "Inelastischer Stoß", frame
