// Diese Datei hat absichtlich Violations — deine Rule soll sie aufspüren.

export function processPayload(payload: any) {
  const result = transform(payload);
  return result;
}

function transform(input: any): any {
  // @ts-ignore
  return input.data.items.map(i => i.value);
}

// TODO: refactor this whole module
export const fetchUser = async (id) => {
  console.log("fetching user", id);
  const response = await fetch(`/api/users/${id}`);
  const data: any = await response.json();
  return data;
};

export function calculatePrice(cart: any) {
  let total = 0;
  for (const item of cart.items) {
    // @ts-ignore
    total += item.price * item.qty;
  }
  console.log("total:", total);
  return total;
}

// TODO: add proper types
export const userDefaults = {
  role: "viewer" as any,
  permissions: [] as any[],
};
