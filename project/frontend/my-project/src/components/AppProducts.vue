<template>
    <section id="products" class="py-16 bg-white">
      <div class="container mx-auto px-6">
        <h2 class="text-4xl font-bold text-center mb-12">Our Products</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
          <ProductCard
            image="/img/out_product.jpg"
            title="AquaPro Filter"
            description="A state-of-the-art water purification system using nanotechnology to remove impurities."
          />
          <ProductCard
            image="/img/max.jpg"
            title="AquaMax Filter"
            description="A reliable solution for homes and offices, ensuring consistent water quality."
          />
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import ProductCard from "./AppProductCard.vue";
  
  export default {
    components: { ProductCard },
  };
  </script>
  