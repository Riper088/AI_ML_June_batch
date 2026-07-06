# --- Part A & B: Spot the Bug & Fix It ---
# The bug: Mutable default argument `cart=[]`. 
# Default arguments are evaluated ONLY ONCE when the function is defined. 
# Therefore, all calls that don't provide a `cart` will share the same list in memory.

# The correct way: Use None and initialize a new list inside.
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

# Let's prove it works correctly now:
print("--- Part B: Fixed add_item ---")
print(add_item_fixed("apple"))    # Expected: ['apple']
print(add_item_fixed("banana"))   # Expected: ['banana'] (not ['apple', 'banana'])
print(add_item_fixed("milk", cart=["bread"])) # Expected: ['bread', 'milk']
print(add_item_fixed("eggs"))     # Expected: ['eggs']


# --- Part C: Build the Cart ---

def create_cart(owner, discount=0):
    """
    Creates a new shopping cart.
    discount=0 is safe because 0 is an immutable integer.
    """
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    """Appends an item dict to the cart's items list."""
    cart["items"].append({"name": name, "price": price, "qty": qty})
    print(f"Added {qty}x {name} to {cart['owner']}'s cart.")

def update_price(price_tuple, new_price):
    """
    Attempt to modify a tuple element.
    Tuples are immutable, so this will raise a TypeError.
    """
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"Expected TypeError caught: {e}")

def calculate_total(cart):
    """Loops over items, sums price * qty, applies discount %, returns total."""
    subtotal = sum(item["price"] * item["qty"] for item in cart["items"])
    discount_amount = subtotal * (cart["discount"] / 100.0)
    final_total = subtotal - discount_amount
    return final_total


if __name__ == "__main__":
    print("\n--- Part C: Shopping Cart Demo ---")
    
    # 1. Create two separate carts
    cart_alice = create_cart("Alice", discount=10)
    cart_bob = create_cart("Bob", discount=0)
    
    # 2. Add items independently
    add_to_cart(cart_alice, "Laptop", 1000, 1)
    add_to_cart(cart_alice, "Mouse", 50, 2)
    
    add_to_cart(cart_bob, "Headphones", 150, 1)
    
    # Prove that the carts don't share the same items list
    print(f"\nAlice's items: {cart_alice['items']}")
    print(f"Bob's items: {cart_bob['items']}")
    
    # 3. Calculate totals
    alice_total = calculate_total(cart_alice)
    bob_total = calculate_total(cart_bob)
    print(f"\nAlice's total (after 10% discount): ${alice_total:.2f}")
    print(f"Bob's total (no discount): ${bob_total:.2f}")
    
    # 4. Demonstrate tuple immutability
    print("\nAttempting to modify a tuple:")
    my_tuple = (100,)
    update_price(my_tuple, 200)

# ==============================================================================
# Discussion Points Answers:
# ==============================================================================
# Q: Why is `discount=0` safe but `cart=[]` dangerous?
# A: `0` is an integer, which is immutable. When evaluated at function definition, 
#    it stores the value 0. If you try to change it inside the function, you are 
#    actually rebinding a new value to the local variable, not modifying the original 0. 
#    `[]` is a mutable list. The function definition creates exactly one list object in 
#    memory, and every call shares that exact same list unless explicitly overridden.
#
# Q: What is the difference between *rebinding* and *mutating*?
# A: Rebinding (e.g. `x = 5`) changes which object the variable points to. 
#    Mutating (e.g. `x.append(5)`) changes the internal state of the existing object 
#    in memory without changing its identity.
#
# Q: Which of these are mutable? — list, tuple, dict, set, str, int
# A: Mutable: list, dict, set
#    Immutable: tuple, str, int
#
# Q: When you pass a list into a function and modify it, do changes reflect outside? Why?
# A: Yes. Python passes variables by object reference (pass-by-assignment). Both the 
#    caller's variable and the function's parameter point to the exact same list in 
#    memory. Mutating the list inside the function changes the shared object.
