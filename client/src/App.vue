<template>
  <div>
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Footer from "@/components/generic/Footer.vue";

export default {
  name: "App",
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style>
.center {
  text-align: center;
}

.make-bold {
  font-weight: bold;
}

.redText {
  color: red;
}

/* Start V-Tooltip CSS */
.tooltip-vue {
  display: block !important;
  z-index: 10000;
}

.tooltip-vue .tooltip-vue-inner {
  background: black;
  color: white;
  border-radius: 5px;
  padding: 5px 10px 4px;
}

.tooltip-vue-arrow {
  width: 0;
  height: 0;
  border-style: solid;
  position: absolute;
  margin: 5px;
  border-color: black;
  z-index: 1;
}

.tooltip-vue[x-placement^="top"] {
  margin-bottom: 5px;
}

.tooltip-vue[x-placement^="top"] .tooltip-vue__arrow {
  border-width: 5px 5px 0 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  bottom: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip-vue[x-placement^="bottom"] {
  margin-top: 5px;
}

.tooltip-vue[x-placement^="bottom"] .tooltip-vue-arrow {
  border-width: 0 5px 5px 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-top-color: transparent !important;
  top: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip-vue[x-placement^="right"] {
  margin-left: 5px;
}

.tooltip-vue[x-placement^="right"] .tooltip-vue__arrow {
  border-width: 5px 5px 5px 0;
  border-left-color: transparent !important;
  border-top-color: transparent !important;
  border-bottom-color: transparent !important;
  left: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip-vue[x-placement^="left"] {
  margin-right: 5px;
}

.tooltip-vue[x-placement^="left"] .tooltip-vue__arrow {
  border-width: 5px 0 5px 5px;
  border-top-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  right: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip-vue[aria-hidden="true"] {
  visibility: hidden;
  opacity: 0;
  transition: opacity 0.15s, visibility 0.15s;
}

.tooltip-vue[aria-hidden="false"] {
  visibility: visible;
  opacity: 1;
  transition: opacity 0.15s;
}

/* END V-Tooltip CSS */
</style>