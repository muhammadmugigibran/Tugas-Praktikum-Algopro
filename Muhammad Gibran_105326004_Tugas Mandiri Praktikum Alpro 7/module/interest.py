def compound_interest(principal, rate, time):
    """Menghitung nilai akhir dengan bunga majemuk."""
    return principal * (1 + rate) ** time

def simple_interest(principal, rate, time):
    """Menghitung nilai akhir dengan bunga sederhana."""
    return principal + (principal * rate * time)