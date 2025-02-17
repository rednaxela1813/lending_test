import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path"; // ✅ Добавляем path для алиасов

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"), // ✅ Добавляем алиас для корректного импорта "@/"
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://backend:8000",
        changeOrigin: true,
        secure: false,
      },
    },
  },
  test: {
    environment: "jsdom", // ✅ Указываем окружение для Vitest
  },
});
