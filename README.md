# CI Datascan Client - Interactive Portfolio

CI Datascan Client is a dynamic and innovative web application that showcases my expertise in software development, tailored for the .NET Developer role for Datascan. This app is a testament to my journey as a .NET Developer, highlighting my skills in React, TypeScrip & UI/UX Design.

## 🚀 About the App

This application serves multiple purposes:
- **Interactive Portfolio**: Demonstrating my technical skills through various code snippets and project examples.
- **Role Exploration**: Providing insights into how my skills and experiences align with the role as .NET developer at Datascan.
- **Developer Journey**: Detailing the development process, challenges faced, and lessons learned.
- **Gift to Interviewers**: A unique takeaway for interview participants, showcasing a complete, live example of my work.

## 🎯 App Features

- **Landing/Thank You Page**: A warm welcome and a note of gratitude to the interviewers and team at [Opportunity/Company Name].
- **Role Description Page**: Tailored content describing how my skills and experience make me a perfect fit for the role.
- **Code Snippets Library**: A curated collection of code examples showcasing my expertise in different areas of software development.
- **Experience Stories Page**: Narratives of my professional experiences and how they relate to the opportunity at hand.
- **Developer Page**: Insights into the development of this application, with interactive demos and code discussions.

## 🛠️ Built With

- React.js
- TypeScript

## 📂 Content Structure

Content for the app is managed dynamically through Markdown files located in the `content` directory. This structure allows for easy updates and customization for different opportunities.

## 🔧 Installation and Setup

Instructions on how to clone, set up, and run the project locally.

```bash
git clone https://github.com/tsmithcad/ci-datascan-client.git
cd ci-datascan-client
npm install
npm start
```

## 📈 Using the App

[Details on how to navigate and interact with the app.]

## 📝 Customizing for Opportunities

[Guidelines on how to adapt the app for different opportunities, including updating Markdown files and specific sections of the app.]

## 🌟 Contributing

Please feel free to contribute, provide feedback, or use the app as a template for your own projects.

## 📬 Feedback and Contact

complementaryintel@gmail.com

---

# Template Notes

## React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default {
  // other rules...
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: ['./tsconfig.json', './tsconfig.node.json'],
    tsconfigRootDir: __dirname,
  },
}
```

- Replace `plugin:@typescript-eslint/recommended` to `plugin:@typescript-eslint/recommended-type-checked` or `plugin:@typescript-eslint/strict-type-checked`
- Optionally add `plugin:@typescript-eslint/stylistic-type-checked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and add `plugin:react/recommended` & `plugin:react/jsx-runtime` to the `extends` list