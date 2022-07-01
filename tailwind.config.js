module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      spacing: {
        "25vh": "25vh",
        "50vh": "50vh",
        "65vh": "65vh",
      },
      width: {
        "9/12": "87.5%"
      },
      keyframes: {
        messageFadeIn: {
          '0%, 100%': {
            opacity: '0',
            transform: 'translateY(-50px)'
          },
          '5%, 95%': {
            opacity: '1',
            transform: 'translateY(50px)'
          }
        }
      },
      animation: {
        messageFadeIn: 'messageFadeIn 5s ease-in-out forwards',
      }
    },
  },
  plugins: [],
}
