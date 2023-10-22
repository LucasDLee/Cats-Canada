<template>
  <footer id="about-footer">
    <a :href="githubProfile" target="_blank"><i class="fab fa-github icon"></i></a>
    <a :href="linkedInProfile" target="_blank"><i class="fab fa-linkedin-in icon"></i></a>
    <a :href="email" target="_blank"><i class="fab fa-google-plus-g icon"></i></a>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      githubProfile: 'https://github.com/LucasDLee',
      githubImg: '/img/github.webp',
      linkedInProfile: 'https://www.linkedin.com/in/lucasdlee',
      linkedInImg: '/img/linkedin.webp',
      email: 'mailto:lucasdlee23@gmail.com',
      emailImg: '/img/email.webp'
    }
  }
}
</script>

<style scoped>
#about-footer {
  background-color: var(--hyperlink-bg-color);
  display: flex;
  flex-direction: row;
  justify-content: center;
  left: 0;
  gap: 0 2em;
  padding: 0.75rem 0;
  position: absolute;
  width: 100vw;
}

#about-footer a {
  width: 50px;
  height: 50px;
  background-color: #fff;
  text-align: center;
  line-height: 50px;
  font-size: 35px;
  margin: 0 10px;
  display: block;
  border-radius: 50%;
  position: relative;
  overflow: hidden;
  border: 3px solid #fff;
  z-index: 1;
}

#about-footer a .icon {
  position: relative;
  color: #262626;
  transition: 0.5s;
  z-index: 3;
}

#about-footer a:hover .icon {
  color: #fff;
  transform: rotateY(360deg);
}

#about-footer a:before {
  content: '';
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  height: 100%;
  background: #f00;
  transition: 0.5s;
  z-index: 2;
}

#about-footer a:hover:before {
  top: 0;
}

#about-footer a:nth-child(1):before {
  /* GitHub */
  background: grey;
}

#about-footer a:nth-child(2):before {
  /* LinkedIn */
  background: #0077b5;
}

#about-footer a:nth-child(3):before {
  /* Google */
  background: linear-gradient(to right, #4285f4, #db4437, #f4b400, #0f9d58);
}
</style>
