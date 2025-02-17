<template>
  <div class="min-h-screen bg-gray-50">
    <Header />
    <main>
      <HeroSection />
      <Products />
      <Technology />
      <ContactForm />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from "./components/AppHeader.vue";
import HeroSection from "./components/HeroSection.vue";
import Products from "./components/AppProducts.vue";
import Technology from "./components/AppTechnology.vue";
import ContactForm from "./components/ContactForm.vue";
import ProductCard from "./components/AppProductCard.vue";
import Footer from "./components/Footer.vue";
import TechFeature from "./components/TechFeature.vue";

export default {
  components: { Header, HeroSection, Products, Technology, ContactForm, Footer },
};
</script>
