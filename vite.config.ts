import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import tailwindcss from '@tailwindcss/vite';

// https://vite.dev/config/
export default defineConfig({
  root: './src/frontend',
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src/frontend/src'),
    },
  },
  publicDir: false,
  build: {
    assetsDir: 'static',
    cssCodeSplit: false,
    outDir: '../templates',
    rolldownOptions: {
      output: {
        assetFileNames: '../static/[name].[ext]',
        inlineDynamicImports: true,
        entryFileNames: '../static/index.js',
      },
    },
  },
});
