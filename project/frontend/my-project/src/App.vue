<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-blue-800 text-white">
      <div class="container mx-auto flex items-center justify-between p-6">
        <div class="flex items-center">
          <!-- Logo: Using a placeholder image for a logo -->
          <img
            src="/img/logo.jpg"
            alt="AquaPure Logo"
            class="h-10 mr-3"
          />
          <span class="text-2xl font-bold">AquaPure Filters</span>
        </div>
        <nav>
          <ul class="flex space-x-6">
            <li><a href="#home" class="hover:underline">Home</a></li>
            <li><a href="#products" class="hover:underline">Products</a></li>
            <li><a href="#technology" class="hover:underline">Technology</a></li>
            <li><a href="#contact" class="hover:underline">Contact</a></li>
          </ul>
        </nav>
      </div>
    </header>

    <main>
      <!-- Hero Section -->
      <section
        id="home"
        class="bg-cover bg-center h-screen flex items-center"
        :style="{ backgroundImage: `url('/img/water.jpg')` }"
      >
        <div class="container mx-auto text-center bg-black bg-opacity-50 p-8 rounded">
          <h1 class="text-5xl font-bold text-white mb-4">Pure Water, Pure Life</h1>
          <p class="text-xl text-white mb-6">
            Innovative water filters by AquaPure Filters.
          </p>
          <a
            href="#contact"
            class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-full transition"
          >
            Get in Touch
          </a>
        </div>
      </section>

      <!-- Products Section -->
      <section id="products" class="py-16 bg-white">
        <div class="container mx-auto px-6">
          <h2 class="text-4xl font-bold text-center mb-12">Our Products</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
            <div class="flex flex-col md:flex-row items-center">
              <!-- Product image 1: Unsplash dynamic image (query with signature to force unique images) -->
              <img
                src="/img/out_product.jpg"
                alt="AquaPro Filter"
                class="w-full md:w-1/2 rounded shadow-lg mb-4 md:mb-0 md:mr-6"
              />
              <div>
                <h3 class="text-2xl font-semibold mb-2">AquaPro Filter</h3>
                <p class="text-gray-700">
                  A state-of-the-art water purification system using nanotechnology to remove impurities.
                </p>
              </div>
            </div>
            <div class="flex flex-col md:flex-row items-center">
              <!-- Product image 2: Unsplash dynamic image -->
              <img
                src="/img/max.jpg"
                alt="AquaMax Filter"
                class="w-full md:w-1/2 rounded shadow-lg mb-4 md:mb-0 md:mr-6"
              />
              <div>
                <h3 class="text-2xl font-semibold mb-2">AquaMax Filter</h3>
                <p class="text-gray-700">
                  A reliable solution for homes and offices, ensuring consistent water quality.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Technology Section -->
      <section id="technology" class="py-16 bg-gray-100">
        <div class="container mx-auto px-6">
          <h2 class="text-4xl font-bold text-center mb-12">Our Technology</h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="text-center p-4">
              <!-- Technology icon -->
              <svg
                class="h-12 w-12 mx-auto text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M9 12l2 2 4-4"></path>
              </svg>
              <h3 class="text-2xl font-semibold mt-4">Nanotechnology</h3>
              <p class="text-gray-600 mt-2">
                Advanced nanomaterials for superior water filtration.
              </p>
            </div>
            <div class="text-center p-4">
              <svg
                class="h-12 w-12 mx-auto text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M9 12l2 2 4-4"></path>
              </svg>
              <h3 class="text-2xl font-semibold mt-4">Eco-Friendly</h3>
              <p class="text-gray-600 mt-2">
                We use environmentally safe materials.
              </p>
            </div>
            <div class="text-center p-4">
              <svg
                class="h-12 w-12 mx-auto text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M9 12l2 2 4-4"></path>
              </svg>
              <h3 class="text-2xl font-semibold mt-4">Efficiency</h3>
              <p class="text-gray-600 mt-2">
                Our filters deliver high-performance purification at every stage.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Contact Section -->
      <section id="contact" class="py-16 bg-white">
        <div class="container mx-auto px-6">
          <h2 class="text-4xl font-bold text-center mb-12">Contact Us</h2>
          <div class="max-w-lg mx-auto">
            <form @submit.prevent="submitForm" class="bg-gray-50 p-8 rounded shadow">
              <div class="mb-4">
                <label for="name" class="block text-gray-700">Your Name</label>
                <input
                  v-model="form.name"
                  id="name"
                  type="text"
                  class="w-full border border-gray-300 p-2 rounded"
                  required
                />
              </div>
              <div class="mb-4">
                <label for="email" class="block text-gray-700">Email</label>
                <input
                  v-model="form.email"
                  id="email"
                  type="email"
                  class="w-full border border-gray-300 p-2 rounded"
                  required
                />
              </div>
              <div class="mb-4">
                <label for="message" class="block text-gray-700">Message</label>
                <textarea
                  v-model="form.message"
                  id="message"
                  rows="4"
                  class="w-full border border-gray-300 p-2 rounded"
                  required
                ></textarea>
              </div>
              <button
                type="submit"
                class="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded transition"
              >
                Send Message
              </button>
            </form>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="bg-blue-800 text-white text-center p-4">
      © 2025 AquaPure Filters. All rights reserved.
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: "",
        email: "",
        message: ""
      }
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/contact/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.form)
        });
        const result = await response.json();
        if (result.status === "success") {
          
          this.form = { name: "", email: "", message: "" };
        } else {
          alert("There was an error sending your message.");
        }
      } catch (error) {
        alert("Error: " + error.message);
      }
    }
  }
};
</script>

<style>
/* Additional styles if needed */
.container {
  max-width: 1200px;
}
</style>
