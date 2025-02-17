<template>
    <section id="technology" class="py-16 bg-gray-100">
      <div class="container mx-auto px-6">
        <h2 class="text-4xl font-bold text-center mb-12">Our Technology</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <TechFeature title="Nanotechnology" description="Advanced nanomaterials for superior water filtration." />
          <TechFeature title="Eco-Friendly" description="We use environmentally safe materials." />
          <TechFeature title="Efficiency" description="Our filters deliver high-performance purification at every stage." />
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import TechFeature from "./TechFeature.vue";
  
  export default {
    components: { TechFeature },
  };
  </script>
  