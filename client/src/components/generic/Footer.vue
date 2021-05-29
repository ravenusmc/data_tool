<template>
  <div>
    <footer>
      <div class="footer_fix">
        <h2 class="footerTitle font">
          Copyright &copy; 2021 Double Sun Productions<br />
          <font-awesome-icon icon="user-secret" size="6x"/>
          <font-awesome-icon icon="UsersCog" size="6x" />
        </h2>
        <!-- <div>
          <a href="https://www.linkedin.com/in/mcuddy1/"
            ><i class="fa fa-linkedin-square fa-3x"></i
          ></a>
          <a href="https://twitter.com/mcuddy7"
            ><i class="fa fa-twitter-square fa-3x" aria-hidden="true"></i
          ></a>
          <a href="https://codingsaga.wordpress.com/"
            ><i class="fa fa-pencil fa-3x" aria-hidden="true"></i
          ></a>
          <a href="https://github.com/ravenusmc"
            ><i class="fa fa-github-square fa-3x" aria-hidden="true"></i
          ></a>
        </div> -->
      </div>
    </footer>
  </div>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { faUsersCog } from '@fortawesome/free-solid-svg-icons'
library.add(faUserSecret)
library.add(faUsersCog)

export default {
  name: "Footer",
};
</script>

<style scoped>
.fa-linkedin-square,
.fa-twitter-square,
.fa-pencil,
.fa-github-square {
  color: black;
  margin: 5px;
}
footer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: black;
  height: 300px;
}
.footer_fix {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 50px;
  padding-top: 50px;
}
.footerTitle {
  color: white;
  font-size: 20px;
  text-transform: uppercase;
  text-align: center;
}

a {
  border: 2px solid white;
}
</style>