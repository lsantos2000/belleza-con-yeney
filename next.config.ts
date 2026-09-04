import type { NextConfig } from 'next';

const nextConfig: NextConfig = process.env.CLOUDFLARE_PAGES_EXPORT === '1'
  ? { output: 'export' }
  : {};

export default nextConfig;
