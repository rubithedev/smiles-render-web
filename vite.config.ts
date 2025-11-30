import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  root: './src/frontend',
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
