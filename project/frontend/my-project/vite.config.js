import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue"; // ✅ Подключаем плагин Vue

export default defineConfig({
  plugins: [vue()], // ✅ Добавляем плагин Vue
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000", // ✅ Прокси на бэкенд
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
