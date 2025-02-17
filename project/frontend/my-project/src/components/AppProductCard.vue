<template>
    <div class="flex flex-col md:flex-row items-center">
      <img :src="image" :alt="title" class="w-full md:w-1/2 rounded shadow-lg mb-4 md:mb-0 md:mr-6" />
      <div>
        <h3 class="text-2xl font-semibold mb-2">{{ title }}</h3>
        <p class="text-gray-700">{{ description }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      image: String,
      title: String,
      description: String,
    },
  };
  </script>
  