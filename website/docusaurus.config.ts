import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const config: Config = {
  title: 'Esame Radioamatori',
  tagline: 'Materiale di studio per la patente di radioamatore',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://iu6vyg.github.io',
  baseUrl: '/esame-radioamatori/',

  organizationName: 'IU6VYG',
  projectName: 'esame-radioamatori',

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'it',
    locales: ['it'],
  },

  markdown: {
    mermaid: true,
    format: 'md',
    hooks: {
      onBrokenMarkdownLinks: 'warn',
      onBrokenMarkdownImages: 'warn',
    },
  },

  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          editUrl:
            'https://github.com/IU6VYG/esame-radioamatori/tree/main/website/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css',
      type: 'text/css',
      integrity:
        'sha384-nB0miv6/jRmo5RLHO8BLeKWilJQbufbCE3jLHXv5S4IWn9OQB5YWtMO0YL3v4U5',
      crossorigin: 'anonymous',
    },
  ],

  themeConfig: {
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Esame Radioamatori',
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'mainSidebar',
          position: 'left',
          label: 'Studio',
        },
        {
          href: 'https://github.com/IU6VYG/esame-radioamatori',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} Esame Radioamatori. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
