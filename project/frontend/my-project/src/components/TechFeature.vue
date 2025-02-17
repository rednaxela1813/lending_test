<template>
    <div class="text-center p-4">
      <svg class="h-12 w-12 mx-auto text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"></path>
      </svg>
      <h3 class="text-2xl font-semibold mt-4">{{ title }}</h3>
      <p class="text-gray-600 mt-2">{{ description }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      description: String,
    },
  };
  </script>
  