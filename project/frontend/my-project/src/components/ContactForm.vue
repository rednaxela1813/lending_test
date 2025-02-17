<template>
  <section id="contact" class="py-16 bg-white">
    <div class="container mx-auto px-6">
      <h2 class="text-4xl font-bold text-center mb-12">Contact Us</h2>
      <div class="max-w-lg mx-auto">
        <form @submit.prevent="submitForm" class="bg-gray-50 p-8 rounded shadow">
          <div class="mb-4">
            <label for="name" class="block text-gray-700">Your Name</label>
            <input v-model="form.name" id="name" type="text" class="w-full border p-2 rounded" required />
          </div>
          <div class="mb-4">
            <label for="email" class="block text-gray-700">Email</label>
            <input v-model="form.email" id="email" type="email" class="w-full border p-2 rounded" required />
          </div>
          <div class="mb-4">
            <label for="message" class="block text-gray-700">Message</label>
            <textarea v-model="form.message" id="message" rows="4" class="w-full border p-2 rounded" required></textarea>
          </div>
          <button type="submit" class="w-full bg-blue-600 text-white py-3 rounded">Send Message</button>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
export default {
data() {
  return {
    form: { name: "", email: "", message: "" },
  };
},
methods: {
  async submitForm() {
  console.log("Отправка данных:", JSON.stringify(this.form));
  console.log("VITE_BACKEND_URL:", import.meta.env.VITE_BACKEND_URL);

  try {
    const backendUrl = import.meta.env.VITE_BACKEND_URL || "http://localhost";
    const apiUrl = `${backendUrl}/api/contact/`; // 👈 Теперь API вызывается на правильном URL

    const response = await fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(this.form),
    });

    const text = await response.text();
    console.log("Ответ сервера (необработанный):", text);

    const result = JSON.parse(text);
    console.log("Ответ сервера (JSON):", result);

    if (!response.ok) {
      alert("Ошибка: " + (result.error || "Неизвестная ошибка"));
      return;
    }

    if (result.status === "success") {
      alert("Сообщение отправлено!");
      this.form = { name: "", email: "", message: "" };
    } else {
      alert("Ошибка: " + result.error);
    }
  } catch (error) {
    alert("Ошибка сети: " + error.message);
  }
}

},
};
</script>
