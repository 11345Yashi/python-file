<!DOCTYPE html>
<!-- saved from url=(0081)https://www.hackerrank.com/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1 -->
<html lang="en" class=" mod_js mod_flexbox mod_flexboxlegacy mod_canvas mod_canvastext mod_webgl mod_no-touch mod_geolocation mod_history mod_draganddrop mod_rgba mod_hsla mod_multiplebgs mod_backgroundsize mod_borderimage mod_borderradius mod_boxshadow mod_textshadow mod_opacity mod_cssanimations mod_csscolumns mod_cssgradients mod_cssreflections mod_csstransforms mod_csstransforms3d mod_csstransitions mod_fontface mod_generatedcontent mod_video mod_audio mod_no-applicationcache mod_svg mod_inlinesvg mod_smil mod_svgclippaths mod_csscalc mod_fullscreen mod_cssresize mod_no-ie8compat"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <script type="text/javascript" async="" src="./product_files/xdc.js.download"></script><script id="twitter-wjs" src="./product_files/widgets.js.download"></script><script src="./product_files/bizible.js.download"></script><script type="text/javascript" async="" src="./product_files/filepicker.js.download"></script><script type="text/javascript" async="" src="./product_files/ga.js.download"></script><script async="" src="./product_files/gtm.js.download"></script><script type="text/javascript">
        function set_manifest(manifest) {
            HR.MANIFEST = manifest;
        }
    </script>
    <script type="text/javascript">
  window.PRODUCT_NAMESPACE = 'hackerrank'
  window.APP_METRIC_TRACKING_ENABLED = false
  window.PERF_METRICS = {
    tracked_initial_view_load_tti: {},
    tracked_view_load_tti: {}
  }
    if ((window.PRODUCT_NAMESPACE == 'hackerrank' || window.PRODUCT_NAMESPACE == 'hackerrankx') && (Math.floor(Math.random() * 2) + 1) == 1) {
      window.APP_METRIC_TRACKING_ENABLED = true
    }
</script>

<script type="text/javascript">
  window.HR = window.HR || {}
  HR.development = false
  HR.production = true
  HR.DESIGN_SUBDOMAIN_PREFIX = 'design'
  HR.DESIGN_DOMAIN = 'hrcdn.net'
  HR.USE_CURRENT_HOST_AS_DESIGN_DOMAIN = ''
  HR.RECAPTCHA_V3_KEY = '6LfTjdkUAAAAAOhQL2_kkpxaLt2mwILWGO9V1_vm'
</script>

<!-- jsCookies -->
  <script type="text/javascript">
    /*!
 * JavaScript Cookie v2.1.2
 * https://github.com/js-cookie/js-cookie
 *
 * Copyright 2006, 2015 Klaus Hartl & Fagner Brack
 * Released under the MIT license
 */
if(function(factory){if("function"==typeof define&&define.amd)define(factory);else if("object"==typeof exports)module.exports=factory();else{var OldCookies=window.Cookies,api=window.Cookies=factory();api.noConflict=function(){return window.Cookies=OldCookies,api}}}(function(){function extend(){for(var i=0,result={};i<arguments.length;i++){var attributes=arguments[i];for(var key in attributes)result[key]=attributes[key]}return result}function init(converter){function api(key,value,attributes){var result;if("undefined"!=typeof document){if(arguments.length>1){if("number"==typeof(attributes=extend({path:"/"},api.defaults,attributes)).expires){var expires=new Date;expires.setMilliseconds(expires.getMilliseconds()+864e5*attributes.expires),attributes.expires=expires}try{result=JSON.stringify(value),/^[\{\[]/.test(result)&&(value=result)}catch(e){}return value=converter.write?converter.write(value,key):encodeURIComponent(String(value)).replace(/%(23|24|26|2B|3A|3C|3E|3D|2F|3F|40|5B|5D|5E|60|7B|7D|7C)/g,decodeURIComponent),key=(key=(key=encodeURIComponent(String(key))).replace(/%(23|24|26|2B|5E|60|7C)/g,decodeURIComponent)).replace(/[\(\)]/g,escape),document.cookie=[key,"=",value,attributes.expires&&"; expires="+attributes.expires.toUTCString(),attributes.path&&"; path="+attributes.path,attributes.domain&&"; domain="+attributes.domain,attributes.secure?"; secure":""].join("")}key||(result={});for(var cookies=document.cookie?document.cookie.split("; "):[],rdecode=/(%[0-9A-Z]{2})+/g,i=0;i<cookies.length;i++){var parts=cookies[i].split("="),cookie=parts.slice(1).join("=");'"'===cookie.charAt(0)&&(cookie=cookie.slice(1,-1));try{var name=parts[0].replace(rdecode,decodeURIComponent);if(cookie=converter.read?converter.read(cookie,name):converter(cookie,name)||cookie.replace(rdecode,decodeURIComponent),this.json)try{cookie=JSON.parse(cookie)}catch(e){}if(key===name){result=cookie;break}key||(result[name]=cookie)}catch(e){}}return result}}return api.set=api,api.get=function(key){return api(key)},api.getJSON=function(){return api.apply({json:!0},[].slice.call(arguments))},api.defaults={},api.remove=function(key,attributes){api(key,"",extend(attributes,{expires:-1}))},api.withConverter=init,api}return init(function(){})}),void 0===jsCookies&&"undefined"!=typeof Cookies)var jsCookies={get:function(c_name){return Cookies.get(c_name)},set:function(c_name,value,expiredays,expirehours,expiremins,expiresecs,options){var exdate=new Date;exdate.setDate(exdate.getDate()+(expiredays||0)),exdate.setHours(exdate.getHours()+(expirehours||0)),exdate.setMinutes(exdate.getMinutes()+(expiremins||0)),exdate.setSeconds(exdate.getSeconds()+(expiresecs||0));var config=options||{};!(null==expiredays&&null==expiresecs&&null==expiremins&&null==expirehours)&&(config.expires=exdate),Cookies.set(c_name,value,config)},check:function(c_name){return!!Cookies.get(c_name)},destroy:function(c_name){Cookies.remove(c_name)}};
  </script>

<script type="text/javascript">
  !function(){function getRandRange(min,max){return parseInt(Math.random()*(max-min))+min}function getRandChar(){var offset=getRandRange(0,35);return offset>25?(offset-26).toString():String.fromCharCode(97+offset)}function makeId(length){for(var text="",i=0;i<length;i++)text+=getRandChar();return text}function setSessionId(){key="session_id";var session_key=jsCookies.get(key);session_key?jsCookies.set(key,session_key,null,2,null,null,{secure:!0}):(epoch=(new Date).getTime(),rand_id=makeId(8),jsCookies.set(key,rand_id+"-"+epoch.toString(),null,2,null,null,{secure:!0})),setTimeout(setSessionId,6e4)}setSessionId()}();
</script>

<!-- DNS Prefetch -->
<link rel="dns-prefetch" href="https://hrcdn.net/">
<link rel="dns-prefetch" href="https://d1ka33fs6lvw5x.cloudfront.net/">
<link rel="dns-prefetch" href="https://notifications.hackerrank.com/">
<link rel="dns-prefetch" href="https://metrics.hackerrank.com/">
<link rel="preconnect" href="https://sentry.io/">
<link rel="dns-prefetch" href="https://sentry.io/">

<!-- use the latest IE browser -->
<meta http-equiv="X-UA-Compatible" content="IE=Edge">

<!-- App Icon for iOS Devices -->
<link rel="apple-touch-icon-precomposed" href="https://hrcdn.net/hackerrank/assets/apple-touch-icon-precomposed-c99b684c98b4befc43c47592bc900ebd95a0b1e9b9e5103b252c8b320432646d.png">

<!-- favicon -->
<link rel="shortcut icon" type="image/png" href="https://hrcdn.net/hackerrank/assets/favicon-69d2a5f80ad413089c703bf9947bfa75582c3f13fdb0a1db26fe5b59d8bfd4ce.png">

<!-- generating meta tags -->


<meta name="description" content="Print the total number of challenges created by hackers.">
<meta property="og:title" content="Solve Challenges">
<meta property="og:image" content="https://hrcdn.net/og/default.jpg">
<meta property="og:description" content="Print the total number of challenges created by hackers. Solving code challenges on HackerRank is one of the best ways to prepare for programming interviews.">
<meta property="og:url" content="https://www.hackerrank.com/contests/t1-aiml2023/challenges">
<meta property="og:site_name" content="HackerRank">
<meta property="og:type" content="hackerrank:challenge">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@hackerrank">
<meta name="twitter:url" content="https://www.hackerrank.com">
<meta name="twitter:title" content="HackerRank">
<meta property="fb:app_id" content="347499128655783">

<link href="https://www.hackerrank.com/contests/t1-aiml2023/challenges/" rel="canonical"><!-- ends meta tags generation -->

<!-- CSRF Token -->
<meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="GAOczwtpPI0nE+NMZ+1G+vYv8JytjwNJiHKJCrM3VizinQVkQp490kqNd/qulb74UVaRzhsw1C0Xc/NdDagYTA==">

  <link rel="stylesheet" media="all" href="./product_files/hackerrank_libraries-aa78a6dc82fad129b5b2c9a5ef5112f854d395f7b3262066ed64d56ed9c4becb.css">
  <link rel="stylesheet" media="all" href="./product_files/hackerrank-core2-3ebb487e9942c5ce4412d25a84e9d46eb085aae02e4abed861aa7dce93e15fb0.css">
  <link rel="stylesheet" media="all" href="./product_files/dashboard-bffe94fa76da102eca7fe83d8ef4060c2901bb713f873d3cd7c8777fd87e4b41.css">
  <link rel="stylesheet" media="all" href="./product_files/theme_m_patch-e8ec223f441200bef3933b0bc08cf5af14f2dd51c173ce984129030357e966c9.css">


<!-- Sentry -->
<!--
CDN distribution of raven.js looks for requirejs, but the module is anonymous.
If we are using require.js and loading an anonymous module without require.js, it raises an error.
https://github.com/getsentry/raven-js/issues/635
https://github.com/getsentry/raven-js/issues/97
-->
  <script src="./product_files/raven-c1b7ecba30517427348abac4ee49e9d81fd04de2247bc9687f530d2c0a719743.js.download" id="raven" crossorigin="anonymous" async="async"></script>
  <script type="text/javascript">
    (function(window, queue, loaded, script) {

      var raven_user_context = {
          handle: '20943573',
      }
      var raven_extra_context = {
        loadTimestamp: 1676568101,
        assetUrl: 'https://hrcdn.net',
        cdnUrl: ''
      }

        raven_extra_context.mixpanel_token = '06a2aa39-71d0-441c-b97f-b1876a3b27b8'

      window.onerror = function e(message, file, lineNo, columnNo, error) {
          if (loaded) return;
          queue.push([message, file, lineNo, columnNo, error]);
      };

      window.onunhandledrejection = function e(error) {
          if (loaded) return;
          queue.push([
              error.reason,
          ]);
      };

      script.onreadystatechange = script.onload = function() {
          if (loaded) return;
          loaded = true;

          Raven.config("https://6b2d52b23d5a4dd4bc44330335327c04@sentry.io/234162", {
              release: '-',
              ignoreUrls: [/cdn\.userty\.com/],
              ignoreErrors: [
                '$ is not defined',
                'Error: Connection is disposed',
                'Connection got disposed',
                'A network error occurred',
                'Model is disposed!',
                'Invalid start index',
              ],
          }).install();
          Raven.setUserContext(raven_user_context)
          Raven.setExtraContext(raven_extra_context)
          window.onunhandledrejection = function e(error) {
              Raven.captureException(error.reason, {
                  extra: {
                      type: error.type,
                  },
              });
          };

          queue.forEach(function(error) {
              Raven.captureException(error[4] || error[0], {
                  extra: {
                      file: error[1],
                      line: error[2],
                      col: error[3],
                  },
              });
          });
      };
    }(window, [], false, document.getElementById('raven')));
  </script>

<!-- Google Analyitics Init -->
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', "UA-45092266-1"]);
    _gaq.push(['_trackPageview']);
    _gaq.push(['_gat._anonymizeIp']);
    _gaq.push(['_setCampSourceKey', 'utm_source']);
    _gaq.push(['_setCampMediumKey', 'utm_medium']);
    _gaq.push(['_setCampContentKey', 'utm_keyword']);
    _gaq.push(['_setCampTermKey', 'utm_keyword']);
    _gaq.push(['_setCampNameKey', 'utm_campaign']);
</script>

<!-- Mixpanel Stub -->
<script type="text/javascript">
  window.mixpanel = window.mixpanel || [];
  var attrs = "disable track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.set_once people.increment people.append people.track_charge people.clear_charges people.delete_user".split(" ");
  for (var attribute in attrs) {
    mixpanel[attrs[attribute]] = function () {};
  }
</script>

<!-- Heap Analytics Init -->
<script type="text/javascript">
    var heap = heap || [];
</script>

<script type="text/javascript">
  (function(h) {
    window.hr_metrics = h;
    if (!h.loaded) {
      var a = ['track', 'batch_track', 'app_track', 'externalService', 'init', 'batch_track_record', 'track_dwell_time', 'set_navigation_data'];
      for (var i = 0; i < a.length; i++) {
        if (!h[a[i]]) {h[a[i]] = function() {};}
      }
    }
  })(window.hr_metrics || {});
</script>

<script type="text/javascript">
    /**
     * Protect window.console method calls, e.g. console is not defined on IE
     * unless dev tools are open, and IE doesn't define console.debug
     */
(function() {
    if (!window.console) {
      window.console = {};
    }
    var m = ["log", "info", "warn", "error", "debug", "trace", "dir", "group", "groupCollapsed", "groupEnd", "time", "timeEnd", "profile", "profileEnd", "dirxml", "assert", "count", "markTimeline", "timeStamp", "clear"];
    // define undefined methods as noops to prevent errors
    for (var i = 0; i < m.length; i++) {
        if (!window.console[m[i]]) {
            window.console[m[i]] = function() {};
        }
    }
})();
</script>


  <script type="text/javascript">
    var pusher_app_key = 'a280047e3b323ccb1b65';
  </script>

<!-- Linkedin Insights -->


<script>
  dataLayer = [];
</script>

<!-- Google Tag Manager #1 -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer', 'GTM-5FXW96J');</script>
<!-- End Google Tag Manager #1 -->


    <!-- General Information -->
    <title>Vowel or Consonant 1 | T1_aiml2023 Question | Contests | HackerRank</title>

    <!--  TODO : This need to be configured from configuration file -->
      <script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="https://hrcdn.net/hackerrank/assets/compound/challenge-views-51f4ee5da60b44948701ff4d06cfcd07b778fd64cafd44989ffbd1c71231fde9.js" src="./product_files/challenge-views-51f4ee5da60b44948701ff4d06cfcd07b778fd64cafd44989ffbd1c71231fde9.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="https://hrcdn.net/hackerrank/assets/codemirror_basic-3e2de7ac8d92f9f64f2f3baf9ba721ba504c9e83979d2a2714cb73d3628ea01a.js" src="./product_files/codemirror_basic-3e2de7ac8d92f9f64f2f3baf9ba721ba504c9e83979d2a2714cb73d3628ea01a.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="https://hrcdn.net/hackerrank/assets/codemirror/mode/python/python-a4643319b4b08ca94742e728df055705837aef74d6309fc3478627f9560c6dbd.js" src="./product_files/python-a4643319b4b08ca94742e728df055705837aef74d6309fc3478627f9560c6dbd.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="https://hrcdn.net/hackerrank/assets/compound/submission-views-1745ff2db40907b8f6477fb42fda4d01f812624e1e0ba1e974bae4fa3a4edeec.js" src="./product_files/submission-views-1745ff2db40907b8f6477fb42fda4d01f812624e1e0ba1e974bae4fa3a4edeec.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="https://hrcdn.net/hackerrank/assets/compound/websocket-libraries-db1a642585285ec6747623cfe7446eefac303beb72c68fc3abe6bca2c411259c.js" src="./product_files/websocket-libraries-db1a642585285ec6747623cfe7446eefac303beb72c68fc3abe6bca2c411259c.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="https://hrcdn.net/hackerrank/assets/compound/game-views-64bc9738d2a7f536c7bfadaf813a8d9f7c143c5f94cdcfcc7b45197175027d2c.js" src="./product_files/game-views-64bc9738d2a7f536c7bfadaf813a8d9f7c143c5f94cdcfcc7b45197175027d2c.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="https://hrcdn.net/hackerrank/assets/codemirror/mode/clike/clike-d8c4990384f4e4eca9386c70f02c44ceede0fa9db101c4ad907543e983e800ec.js" src="./product_files/clike-d8c4990384f4e4eca9386c70f02c44ceede0fa9db101c4ad907543e983e800ec.js.download"></script><!--<base href="/">--><base href=".">

    <script type="text/javascript">
      var HR;
      HR = window.HR || {};
      HR.PREFETCH_DATA = {"metadata":{"asset_path":"https://hrcdn.net/hackerrank/assets","asset_host":"https://hrcdn.net","asset_host_path":"https://hrcdn.net/hackerrank","filepicker_key":"ApehXMbvXTWqWab7OmMr9z","pubsub_host":"https://pubsub.hackerrank.com","pubsubv2_host":"https://pubsubv2.hackerrank.com","release_version":"0","country_from_ip":null,"landing_contest_slug":"t1-aiml2023","current_contest_namespace":"/contests/t1-aiml2023","using_contest_namespace":true},"slugs":{"t1-aiml2023":{"type":"contest"},"yashasvinitripa1":{"type":"hacker"}},"contest":{"id":193157,"name":"T1_aiml2023","slug":"t1-aiml2023","created_at":"2022-10-08T18:00:44.000Z","updated_at":"2023-02-08T04:01:49.000Z","starttime":"2023-02-08T03:30:00.000Z","endtime":"2023-03-30T05:30:00.000Z","timezone":"PST","homepage":null,"tagline":null,"description":"Please provide a short description of your contest here! This will also be used as metadata.","homepage_background_color":null,"notification":null,"template_id":552,"expose_stats":null,"public":false,"team_event":false,"rating_category":null,"is_rating_updated":false,"leaderboard_backend":null,"leaderboard_format":"","primary_track_id":null,"college_public":null,"rated":null,"is_multi_round":false,"parent_contest_id":null,"primary_tag_id":null,"started":true,"ended":false,"epoch_endtime":1680154200,"epoch_starttime":1675827000,"time_left":3586098.93451704,"hide_difficulty":null,"has_tracks":null,"archived":false,"leaderboard_type":"country","kind":"","leaderboard_freeze_time":null,"show_penalty":true,"track":null,"hide_navigation":null,"contest_broadcast":null,"hide_leaderboard":null,"hide_submissions":null,"leaderboard_out_of_sync":null,"leaderboard_out_of_sync_message":null,"challenges_count":9,"show_participants_info":null,"custom_leaderboard_column_name":null,"disable_forum":null,"disable_fsi":null,"has_codesprint_reg_page":null,"hidden":null,"comment_live_sync":null,"company_associated_contest":null,"limited_participants":null,"leaderboard_broadcast_message":null,"qualification_rule_type":null,"qualification_rule_value":0,"qualification_rule_msg":null,"migration_status":null,"migration_disabled":null,"testers_contest":null,"time_limited_contest":false,"hacker_timelimit":null,"school_leaderboard_enabled":false,"organization_type":"GLA university","organization_name":"GLA university","sponsor_logos":null,"sponsor_logos_name":null,"require_linkedin_or_resume":null,"effective_time_left":3586098.932402267,"effective_epoch_endtime":1680154200},"messages":[],"profile":{"id":20943573,"username":"yashasvinitripa1","country":"India","school":null,"languages":[["python3","10"],["pypy3","7"]],"created_at":"2023-02-09T21:30:48.000Z","level":1,"email":"yashasvinitripathi@gmail.com","fb_uid":null,"gh_uid":null,"li_uid":null,"is_admin":false,"support_admin":false,"avatar":"https://d1ce3iv5vajdy.cloudfront.net/hackerrank/assets/gravatar.jpg","website":"","short_bio":null,"username_change_count":null,"name":"Yashasvini Tripathi","personal_first_name":"Yashasvini","personal_last_name":"Tripathi","company":"","local_language":null,"has_avatar_url":false,"hide_account_checklist":null,"spam_user":null,"job_title":"","jobs_headline":null,"linkedin_url":null,"github_url":null,"errors":{},"confirmed":false,"facebook_allow_opengraph":null,"tsize":null,"is_migrated":false,"facebook_opengraph_access_available":null,"promised_login_time":null,"last_logout_feedback":null,"chat_enabled":true,"tour_done":null,"username_autoset":true,"key_prefix":"20943573-8a6981055ec4443f55df62c3fe706225e33e3a2a","notifications_url":"https://notify.hackerrank.com/subscribe/20943573-e4a3f7ffabf9223e2a58df95185c60c61725835c","resume_url":null,"relocate":null,"phone":null,"phone_number":null,"blog_url":null,"college_major":null,"college_major_id":null,"jobs_consent":null,"graduation_year":null,"graduation_month":null,"college_year":null,"college_majors":null,"intro_screen_onboarding_done":null,"related_topics_tour_done":null,"company_challenge_breadcrumb_tour_done":null,"contest_reminders_banner_selected":null,"hometown":null,"employment_title":null,"employment_years":null,"college_roll_no":null,"college_semester":null,"college_course":null,"college_cgpa":null,"city":"Mathura","state":null,"username_change_max":2,"has_viewed_feed_page":null,"address":null,"has_verified_phone_number":false,"country_of_residence":null,"has_seen_ch_full_screen_intro":null,"experience_status":null,"address_line2":null,"address_city":null,"address_state":null,"address_zip":null,"us_work_eligibility":null,"us_work_eligibility_2":null,"is_professional":false,"years_of_experience":null,"us_citizenship":null,"us_citizenship_2":null,"gender":null,"is_campus_rep":false,"hacko_amount":224,"timezone":"Asia/Calcutta","us_work_prefs":null,"ethnicity":null,"jobs_joining_date":null,"jobs_prefered_roles":null,"jobs_top_skills":null,"state_id":null,"jobs_complete_us_visa":null,"jobs_us_visa_other":null,"uk_work_eligibility":null,"stryker_consent":null,"work_ex_reset_flag":null,"job_board_consent":null,"is_organizer":null,"bookmarks_count":0,"role_number":null,"dashboard_survey_preference":null,"has_solved_a_challenge":true,"status_solve_me_first":null,"source":null,"track_nux_mixpanel":null,"registration_custom_data":null,"preferred_lang":null,"badges_onboarding_status":null,"updated_modal_profiled_data":null,"badges_opt_in_status":null,"tos_accepted_on":1675978248,"tried_interview_prep":null,"hacker_pubsub_channel":"20943573-e4a3f7ffabf9223e2a58df95185c60c61725835c","tried_monaco_editor":null,"ga_user_id":"520b31a4e4930a814ea1de0859d35bf8681c8d54","ga_client_id":"1338819460.1667380436","ga_user_ip":"2001:df7:0:5168:a06b:de27:55eb:650e","job_seeking_intent_survey":null,"job_survey_professional_data_required":2,"sourcing_jobs_consent":false,"work_start_year":null,"is_high_school_student":false,"dark_mode_banner_seen":null,"dark_mode_seen":null,"is_linkedin_connected":false,"job_availability_type":null,"job_availability_year":null,"vcf_profile_visibility":null,"signup_intent":"prepare","onboarding_status":"done","work_authorization_countries":null,"user_prefers_theme":"light","tos_accepted":true,"show_dashboard_v2":true,"show_mock_tests":false,"show_certificates":false,"show_recommended_prep_kit":false,"show_prep_kits":true,"show_dashboard_banner":true,"show_codecademy_integration":false,"show_dark_theme":true,"show_challenge_v2":false,"show_pubsub_socketio":false,"secondary_emails":[]},"timestamp":1676568101,"tracks":[{"id":24,"slug":"tutorials","name":"Tutorials","chapters":[{"id":146,"name":"30 Days of Code","slug":"30-days-of-code","hidden":false},{"id":147,"name":"10 Days of Statistics","slug":"10-days-of-statistics","hidden":false},{"id":148,"name":"10 Days of Javascript","slug":"10-days-of-javascript","hidden":false}],"selected":2},{"id":3,"slug":"algorithms","name":"Algorithms","chapters":[{"id":43,"name":"Warmup","slug":"warmup","hidden":false},{"id":108,"name":"Implementation","slug":"implementation","hidden":false},{"id":34,"name":"Strings","slug":"strings","hidden":false},{"id":38,"name":"Sorting","slug":"arrays-and-sorting","hidden":false},{"id":36,"name":"Search","slug":"search","hidden":false},{"id":33,"name":"Graph Theory","slug":"graph-theory","hidden":false},{"id":59,"name":"Greedy","slug":"greedy","hidden":false},{"id":35,"name":"Dynamic Programming","slug":"dynamic-programming","hidden":false},{"id":151,"name":"Constructive Algorithms","slug":"constructive-algorithms","hidden":false},{"id":30,"name":"Bit Manipulation","slug":"bit-manipulation","hidden":false},{"id":153,"name":"Recursion","slug":"recursion","hidden":false},{"id":47,"name":"Game Theory","slug":"game-theory","hidden":false},{"id":29,"name":"NP Complete","slug":"np-complete-problems","hidden":false},{"id":161,"name":"Debugging","slug":"algo-debugging","hidden":false}],"selected":2},{"id":17,"slug":"data-structures","name":"Data Structures","chapters":[{"id":134,"name":"Arrays","slug":"arrays","hidden":false},{"id":39,"name":"Linked Lists","slug":"linked-lists","hidden":false},{"id":96,"name":"Trees","slug":"trees","hidden":false},{"id":119,"name":"Balanced Trees","slug":"balanced-trees","hidden":false},{"id":97,"name":"Stacks","slug":"stacks","hidden":false},{"id":98,"name":"Queues","slug":"queues","hidden":false},{"id":99,"name":"Heap","slug":"heap","hidden":false},{"id":100,"name":"Disjoint Set","slug":"disjoint-set","hidden":false},{"id":113,"name":"Multiple Choice","slug":"multiple-choice","hidden":false},{"id":118,"name":"Trie","slug":"trie","hidden":false},{"id":32,"name":"Advanced","slug":"data-structures","hidden":false}],"selected":2},{"id":22,"slug":"mathematics","name":"Mathematics","chapters":[{"id":109,"name":"Fundamentals","slug":"fundamentals","hidden":false},{"id":52,"name":"Number Theory","slug":"number-theory","hidden":false},{"id":51,"name":"Combinatorics","slug":"combinatorics","hidden":false},{"id":55,"name":"Algebra","slug":"algebra","hidden":false},{"id":54,"name":"Geometry","slug":"geometry","hidden":false},{"id":53,"name":"Probability","slug":"probability","hidden":false},{"id":128,"name":"Linear Algebra Foundations","slug":"linear-algebra-foundations","hidden":false}],"selected":2},{"id":27,"slug":"c","name":"C","chapters":[{"id":154,"name":"Introduction","slug":"c-introduction","hidden":false},{"id":155,"name":"Conditionals and Loops","slug":"c-conditionals-and-loops","hidden":false},{"id":156,"name":"Arrays and Strings","slug":"c-arrays-and-strings","hidden":false},{"id":157,"name":"Functions","slug":"c-functions","hidden":false},{"id":158,"name":"Structs and Enums","slug":"c-structs-and-enums","hidden":false}],"selected":2},{"id":2,"slug":"ai","name":"Artificial Intelligence","chapters":[{"id":8,"name":"Bot Building","slug":"ai-introduction","hidden":false},{"id":9,"name":"A* Search","slug":"astar-search","hidden":false},{"id":10,"name":"Alpha Beta Pruning","slug":"alpha-beta-pruning","hidden":false},{"id":14,"name":"Combinatorial Search","slug":"combinatorial-search-theory","hidden":false},{"id":13,"name":"Games","slug":"richman-games","hidden":false},{"id":11,"name":"Statistics and Machine Learning","slug":"machine-learning","hidden":false},{"id":44,"name":"Digital Image Analysis","slug":"image-analysis","hidden":false},{"id":49,"name":"Natural Language Processing","slug":"nlp","hidden":false},{"id":129,"name":"Probability \u0026 Statistics - Foundations","slug":"statistics-foundations","hidden":false}],"selected":2},{"id":13,"slug":"cpp","name":"C++","chapters":[{"id":77,"name":"Introduction","slug":"cpp-introduction","hidden":false},{"id":76,"name":"Strings","slug":"cpp-strings","hidden":false},{"id":78,"name":"Classes","slug":"classes","hidden":false},{"id":116,"name":"STL","slug":"stl","hidden":false},{"id":127,"name":"Inheritance","slug":"inheritance","hidden":false},{"id":159,"name":"Debugging","slug":"cpp-debugging","hidden":false},{"id":152,"name":"Other Concepts","slug":"other-concepts","hidden":false}],"selected":2},{"id":15,"slug":"java","name":"Java","chapters":[{"id":80,"name":"Introduction","slug":"java-introduction","hidden":false},{"id":82,"name":"Strings","slug":"java-strings","hidden":false},{"id":83,"name":"BigNumber","slug":"bignumber","hidden":false},{"id":84,"name":"Data Structures","slug":"java-data-structure","hidden":false},{"id":85,"name":"Object Oriented Programming","slug":"oop","hidden":false},{"id":106,"name":"Exception Handling","slug":"handling-exceptions","hidden":false},{"id":136,"name":"Advanced","slug":"java-advanced","hidden":false}],"selected":2},{"id":12,"slug":"python","name":"Python","chapters":[{"id":73,"name":"Introduction","slug":"py-introduction","hidden":false},{"id":74,"name":"Basic Data Types","slug":"py-basic-data-types","hidden":false},{"id":75,"name":"Strings","slug":"py-strings","hidden":false},{"id":120,"name":"Sets","slug":"py-sets","hidden":false},{"id":121,"name":"Math","slug":"py-math","hidden":false},{"id":122,"name":"Itertools","slug":"py-itertools","hidden":false},{"id":123,"name":"Collections","slug":"py-collections","hidden":false},{"id":124,"name":"Date and Time","slug":"py-date-time","hidden":false},{"id":126,"name":"Errors and Exceptions","slug":"errors-exceptions","hidden":false},{"id":42,"name":"Classes","slug":"py-classes","hidden":false},{"id":125,"name":"Built-Ins","slug":"py-built-ins","hidden":false},{"id":87,"name":"Python Functionals","slug":"py-functionals","hidden":false},{"id":88,"name":"Regex and Parsing","slug":"py-regex","hidden":false},{"id":89,"name":"XML","slug":"xml","hidden":false},{"id":90,"name":"Closures and Decorators","slug":"closures-and-decorators","hidden":false},{"id":139,"name":"Numpy","slug":"numpy","hidden":false},{"id":160,"name":"Debugging","slug":"py-debugging","hidden":false}],"selected":2},{"id":14,"slug":"ruby","name":"Ruby","chapters":[{"id":72,"name":"Introduction","slug":"ruby-tutorials","hidden":false},{"id":86,"name":"Control Structures","slug":"control-structures","hidden":false},{"id":79,"name":"Arrays \u0026 Hashes","slug":"ruby-arrays","hidden":false},{"id":107,"name":"Enumerables","slug":"ruby-enumerables","hidden":false},{"id":112,"name":"Methods","slug":"ruby-methods","hidden":false},{"id":135,"name":"Strings","slug":"ruby-strings","hidden":false}],"selected":2},{"id":18,"slug":"sql","name":"SQL","chapters":[{"id":92,"name":"Basic Select","slug":"select","hidden":false},{"id":132,"name":"Advanced Select","slug":"advanced-select","hidden":false},{"id":95,"name":"Aggregation","slug":"aggregation","hidden":false},{"id":94,"name":"Basic Join","slug":"join","hidden":false},{"id":133,"name":"Advanced Join","slug":"advanced-join","hidden":false},{"id":143,"name":"Alternative Queries","slug":"alternative-queries","hidden":false}],"selected":2},{"id":16,"slug":"databases","name":"Databases","chapters":[{"id":91,"name":"Relational Algebra","slug":"relational-algebra","hidden":false},{"id":93,"name":"Indexes","slug":"indexes","hidden":false},{"id":117,"name":"OLAP","slug":"olap","hidden":false},{"id":101,"name":"Set and Algebra","slug":"set-and-algebra","hidden":false},{"id":130,"name":"NoSQL - XML, MapReduce","slug":"xpath-queries","hidden":false},{"id":131,"name":"Database Normalization","slug":"database-normalization","hidden":false}],"selected":2},{"id":21,"slug":"distributed-systems","name":"Distributed Systems","chapters":[{"id":103,"name":"Multiple Choice","slug":"distributed-mcq","hidden":false},{"id":104,"name":"Client Server","slug":"client-server","hidden":false},{"id":111,"name":"MapReduce Basics","slug":"mapreduce-basics","hidden":false}],"selected":2},{"id":6,"slug":"shell","name":"Linux Shell","chapters":[{"id":56,"name":"Bash","slug":"bash","hidden":false},{"id":57,"name":"Text Processing","slug":"textpro","hidden":false},{"id":114,"name":"Arrays in Bash","slug":"arrays-in-bash","hidden":false},{"id":115,"name":"Grep Sed Awk","slug":"grep-sed-awk","hidden":false}],"selected":2},{"id":5,"slug":"fp","name":"Functional Programming","chapters":[{"id":27,"name":"Introduction","slug":"intro","hidden":false},{"id":26,"name":"Recursion","slug":"fp-recursion","hidden":false},{"id":45,"name":"Functional Structures","slug":"ds","hidden":false},{"id":40,"name":"Memoization and DP","slug":"dp","hidden":false},{"id":50,"name":"Persistent Structures","slug":"persistent-ds","hidden":false},{"id":41,"name":"Ad Hoc","slug":"misc","hidden":false},{"id":46,"name":"Parsers","slug":"parsers","hidden":false},{"id":48,"name":"Interpreter and Compilers","slug":"compilers","hidden":false}],"selected":2},{"id":19,"slug":"regex","name":"Regex","chapters":[{"id":137,"name":"Introduction","slug":"re-introduction","hidden":false},{"id":141,"name":"Character Class","slug":"re-character-class","hidden":false},{"id":142,"name":"Repetitions","slug":"re-repetitions","hidden":false},{"id":140,"name":"Grouping and Capturing","slug":"grouping-and-capturing","hidden":false},{"id":144,"name":"Backreferences","slug":"backreferences","hidden":false},{"id":145,"name":"Assertions","slug":"assertions","hidden":false},{"id":138,"name":"Applications","slug":"re-applications","hidden":false}],"selected":2},{"id":26,"slug":"general-programming","name":"General Programming","chapters":[],"selected":2},{"id":20,"slug":"security","name":"Security","chapters":[{"id":102,"name":"Functions","slug":"functions","hidden":false},{"id":105,"name":"Terminology and Concepts","slug":"concepts","hidden":false},{"id":31,"name":"Cryptography","slug":"cryptography","hidden":false}],"selected":2}],"ab_tests":{"models":[{"id":122,"name":"react_migration","product":1,"variants":[{"id":372,"weight":0,"variant":"trm0","active":false},{"id":373,"weight":1,"variant":"trm1","active":false},{"id":374,"weight":1,"variant":"cnt1","active":false},{"id":375,"weight":4,"variant":"trm2","active":false},{"id":376,"weight":4,"variant":"cnt2","active":false},{"id":377,"weight":5,"variant":"trm3","active":false},{"id":378,"weight":5,"variant":"cnt3","active":false},{"id":379,"weight":10,"variant":"trm4","active":false},{"id":380,"weight":10,"variant":"cnt4","active":false},{"id":381,"weight":10,"variant":"trm5","active":false},{"id":382,"weight":10,"variant":"cnt5","active":false},{"id":383,"weight":20,"variant":"trm6","active":false},{"id":384,"weight":20,"variant":"cnt6","active":false}],"hacker_variant":{"variant":"cnt6","forced":false}},{"id":240,"name":"skills-verification-card-text","product":1,"variants":[{"id":997,"weight":20,"variant":"text_1","active":false},{"id":998,"weight":20,"variant":"text_2","active":false},{"id":999,"weight":20,"variant":"text_3","active":false},{"id":1000,"weight":20,"variant":"text_4","active":false},{"id":1001,"weight":20,"variant":"text_5","active":false}],"hacker_variant":{"variant":"text_4","forced":false}},{"id":246,"name":"mock-tests","product":1,"variants":[{"id":1055,"weight":0,"variant":"show0","active":true},{"id":1056,"weight":2,"variant":"show1","active":true},{"id":1057,"weight":2,"variant":"dont_show1","active":false},{"id":1058,"weight":3,"variant":"show2","active":false},{"id":1059,"weight":3,"variant":"dont_show2","active":false},{"id":1060,"weight":5,"variant":"show3","active":false},{"id":1061,"weight":5,"variant":"dont_show3","active":false},{"id":1062,"weight":40,"variant":"show4","active":false},{"id":1063,"weight":40,"variant":"dont_show4","active":false}],"hacker_variant":{"variant":"show1","forced":false}},{"id":247,"name":"onboarding-survey","product":1,"variants":[{"id":1064,"weight":0,"variant":"control0","active":false},{"id":1065,"weight":0,"variant":"treatment0","active":false},{"id":1066,"weight":1,"variant":"treatment1","active":false},{"id":1067,"weight":1,"variant":"control1","active":false},{"id":1068,"weight":4,"variant":"treatment2","active":false},{"id":1069,"weight":4,"variant":"control2","active":false},{"id":1070,"weight":5,"variant":"treatment3","active":false},{"id":1071,"weight":5,"variant":"control3","active":false},{"id":1072,"weight":10,"variant":"treatment4","active":false},{"id":1073,"weight":10,"variant":"control4","active":false},{"id":1074,"weight":10,"variant":"treatment5","active":false},{"id":1075,"weight":10,"variant":"control5","active":false},{"id":1076,"weight":20,"variant":"treatment6","active":false},{"id":1077,"weight":20,"variant":"control6","active":false}],"hacker_variant":{"variant":"treatment2","forced":false}},{"id":248,"name":"dashboard-v2","product":1,"variants":[{"id":1078,"weight":0,"variant":"treatment0","active":true},{"id":1079,"weight":0,"variant":"control0","active":true},{"id":1080,"weight":1,"variant":"treatment1","active":true},{"id":1081,"weight":1,"variant":"control1","active":true},{"id":1082,"weight":4,"variant":"treatment2","active":true},{"id":1083,"weight":4,"variant":"control2","active":true},{"id":1084,"weight":5,"variant":"treatment3","active":true},{"id":1085,"weight":5,"variant":"control3","active":true},{"id":1086,"weight":20,"variant":"treatment4","active":true},{"id":1087,"weight":20,"variant":"control4","active":true},{"id":1088,"weight":20,"variant":"treatment5","active":true},{"id":1089,"weight":20,"variant":"control5","active":true}],"hacker_variant":{"variant":"treatment4","forced":false}},{"id":249,"name":"codecademy-integration","product":1,"variants":[{"id":1090,"weight":0,"variant":"treatment0","active":true},{"id":1091,"weight":0,"variant":"control0","active":false},{"id":1092,"weight":1,"variant":"treatment1","active":true},{"id":1093,"weight":1,"variant":"control1","active":false},{"id":1094,"weight":4,"variant":"treatment2","active":true},{"id":1095,"weight":4,"variant":"control2","active":false},{"id":1096,"weight":5,"variant":"treatment3","active":true},{"id":1097,"weight":5,"variant":"control3","active":false},{"id":1098,"weight":20,"variant":"treatment4","active":true},{"id":1099,"weight":20,"variant":"control4","active":false},{"id":1100,"weight":20,"variant":"treatment5","active":false},{"id":1101,"weight":20,"variant":"control5","active":false}],"hacker_variant":{"variant":"control4","forced":false}},{"id":250,"name":"show_full_screen_editor","product":1,"variants":[{"id":1102,"weight":0,"variant":"treatment0","active":true},{"id":1103,"weight":0,"variant":"control0","active":true},{"id":1104,"weight":1,"variant":"treatment1","active":true},{"id":1105,"weight":1,"variant":"control1","active":true},{"id":1106,"weight":4,"variant":"treatment2","active":true},{"id":1107,"weight":4,"variant":"control2","active":true},{"id":1108,"weight":5,"variant":"treatment3","active":true},{"id":1109,"weight":5,"variant":"control3","active":true},{"id":1110,"weight":20,"variant":"treatment4","active":true},{"id":1111,"weight":20,"variant":"control4","active":true},{"id":1112,"weight":20,"variant":"treatment5","active":true},{"id":1113,"weight":20,"variant":"control5","active":true}],"hacker_variant":{"variant":"control5","forced":false}},{"id":251,"name":"show_dark_theme","product":1,"variants":[{"id":1114,"weight":0,"variant":"treatment0","active":true},{"id":1115,"weight":0,"variant":"control0","active":false},{"id":1116,"weight":1,"variant":"treatment1","active":true},{"id":1117,"weight":1,"variant":"control1","active":false},{"id":1118,"weight":4,"variant":"treatment2","active":true},{"id":1119,"weight":4,"variant":"control2","active":false},{"id":1120,"weight":5,"variant":"treatment3","active":true},{"id":1121,"weight":5,"variant":"control3","active":false},{"id":1122,"weight":20,"variant":"treatment4","active":true},{"id":1123,"weight":20,"variant":"control4","active":false},{"id":1124,"weight":20,"variant":"treatment5","active":true},{"id":1125,"weight":20,"variant":"control5","active":false}],"hacker_variant":{"variant":"treatment4","forced":false}},{"id":252,"name":"pubsub-socketio","product":1,"variants":[{"id":1126,"weight":0,"variant":"treatment0","active":true},{"id":1127,"weight":0,"variant":"control0","active":false},{"id":1128,"weight":1,"variant":"treatment1","active":true},{"id":1129,"weight":1,"variant":"control1","active":false},{"id":1130,"weight":4,"variant":"treatment2","active":true},{"id":1131,"weight":4,"variant":"control2","active":false},{"id":1132,"weight":5,"variant":"treatment3","active":true},{"id":1133,"weight":5,"variant":"control3","active":false},{"id":1134,"weight":20,"variant":"treatment4","active":false},{"id":1135,"weight":20,"variant":"control4","active":false},{"id":1136,"weight":20,"variant":"treatment5","active":false},{"id":1137,"weight":20,"variant":"control5","active":false}],"hacker_variant":{"variant":"control5","forced":false}},{"id":254,"name":"hackerresume-adunits1","product":1,"variants":[{"id":1140,"weight":75,"variant":"control","active":false},{"id":1141,"weight":25,"variant":"showCard","active":false}],"hacker_variant":{"variant":"control","forced":false}},{"id":255,"name":"hrc-app-drawer","product":1,"variants":[{"id":1142,"weight":0,"variant":"control","active":false},{"id":1143,"weight":100,"variant":"showAppDrawer","active":false}],"hacker_variant":{"variant":"showAppDrawer","forced":false}}]},"in_maintenance_mode":false,"maintenance_details":{"notification_start":1495931400,"maintenance_start":1496017800,"maintenance_end":1496021400,"api_message":"We are performing scheduled maintenance on our servers. Please refer to https://updates.hackerrank.com/scheduled-maintenance-on-may-28th-2018-at-530pm-pt/ for more details."},"feature_feedback_list":[],"admin_su":null,"badge_map":{"algorithms":["problem-solving"],"data-structures":["problem-solving"],"cpp":["cpp"],"java":["java"],"python":["python"],"sql":["sql"],"c":["c"],"ruby":["ruby"],"30-days-of-code":["30-days-of-code"],"10-days-of-javascript":["10-days-of-javascript"],"10-days-of-statistics":["10-days-of-statistics"]},"feature_flags":{}};
      HR.MANIFEST_HASH = "43521ec957bc6ed66f0adfeb06022b8497dfaf57";
    </script>

    <link rel="alternate" type="application/rss+xml" title="RSS" href="https://www.hackerrank.com/rest/blogs.rss">
<style type="text/css">.fp__btn{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline-block;height:34px;padding:4px 30px 5px 40px;position:relative;margin-bottom:0;vertical-align:middle;-ms-touch-action:manipulation;touch-action:manipulation;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;font-family:"Open Sans", sans-serif;font-size:12px;font-weight:600;line-height:1.42857143;color:#fff;text-align:center;white-space:nowrap;background:#ef4925;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAVCAYAAABLy77vAAAABGdBTUEAALGPC/xhBQAAAJRJREFUOBHNUcEWgCAIy14fbl9egK5MRarHQS7ocANmOCgWh1gdNERig1CgwPlLxkZuE80ndHlU+4Lda1zz0m01dSKtcz0h7qpQb7WR+HyrqRPxahzwwMqqkEVs6qnv+86NQAbcJlK/X+vMeMe7XcBOYaRzcbItUR7/8QgcykmElQrQPErnmxNxl2yyiwcgEvQUocIJaE6yERwqXDIAAAAASUVORK5CYII=");background-repeat:no-repeat;background-position:15px 6px;border:1px solid transparent;border-radius:17px}.fp__btn:hover{background-color:#d64533}.fp__btn::after{position:absolute;content:"";top:15px;right:14px;width:7px;height:4px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAICAYAAAA1BOUGAAAABGdBTUEAALGPC/xhBQAAAGlJREFUCB1j/P//vw4DA4MiEKOD+0xAkatA/AJNBsS/ysTIyPgfyDgHxO+hCkD0Oag4RAhoPDsQm4NoqCIGBiBnAhBjAxNAkkxAvBZNFsQHuQesmxPIOQZVAKI54UZDFYgABbcBsQhMAgDIVGYSqZsn6wAAAABJRU5ErkJggg==");}.fp__btn:hover::after{background-position:0 -4px;}.fp__btn:active,.fp__btn:focus{outline:none}@media only screen and (min--moz-device-pixel-ratio: 2), only screen and (-o-min-device-pixel-ratio: 2 / 1), only screen and (-webkit-min-device-pixel-ratio: 2), only screen and (min-device-pixel-ratio: 2){.fp__btn{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAqCAYAAADbCvnoAAAABGdBTUEAALGPC/xhBQAAAQFJREFUWAntWEESwjAIbBwfHl+upNoRNjKUJhk5kIvZQGG7bHOwPGltgdYtEJedShKyJnLHhEILz1Zi9HCOzFI7FUqFLAWseDgPdfeQ9QZ4b1j53nstnEJJyBqx20NeT1gEMB5uZG6Fzn5lV5UMp1ASQhMjdnvoqjewsYbDjcytEH5lsxULp1AS0sx8nJfVnjganf3NkVlKhVPIfQ9Zb6jF0atK3mNriXwpicPHvIeyr3sTDA53VgpgH8BvMu1ZCCz7ew/7MPwlE4CQJPNnQj2ZX4SYlEPbVpsvKFZ5TOwhcRoUTQiwwhVjArPEqVvRhMCneMXzDk9lwYphIwrZZOihF32oehMAa1qSAAAAAElFTkSuQmCC");background-size:18px 21px}.fp__btn::after{background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAQCAYAAAAmlE46AAAABGdBTUEAALGPC/xhBQAAANpJREFUKBWVkU8KglAYxJ/u3HuBwmUX8BqepKN4ka4RguDOVYu2QVCrhIJ6/caekqLiGxi+PzPD58PAWrszxmygD84h7hpePFLy1mEQBJamgvcVYXkqZXTR0LwpJWw0z0Ba6bymDcrI4kkp4EvzCNoVztNKfVATwoOiyx/NDup1SVqPQVBbDDeK3txBb9JuHfhNW3HWjZhDX+SGRAgPHkl5f0+kieBxRVieaPD5LGJ4WghLiwehbkBI4HUirF3S+SYrhhQ2f2H16aR5vMSYwbdjNtYXZ0J7cc70BXnFMHIGznzEAAAAAElFTkSuQmCC");background-size:7px 8px;}}</style></head>

<body id="hr_v2" class="show-cookie-banner" itemscope="" itemtype="http://schema.org/WebPage" style="zoom: 1;">
      <div class="cdn-error-view" style="display:none;">
  <div class="error-box-wrap">
    <div class="error-icon">
      <svg x="0px" y="0px" width="80px" height="80px" viewBox="0 0 367.011 367.01" style="enable-background:new 0 0 367.011 367.01;" xml:space="preserve">
        <g>
         <g>
          <path d="M365.221,329.641L190.943,27.788c-1.542-2.674-4.395-4.318-7.479-4.318c-3.084,0-5.938,1.645-7.48,4.318L1.157,330.584    c-1.543,2.674-1.543,5.965,0,8.639c1.542,2.674,4.395,4.318,7.48,4.318h349.65c0.028,0,0.057,0,0.086,0    c4.77,0,8.638-3.863,8.638-8.639C367.011,332.92,366.342,331.1,365.221,329.641z M23.599,326.266L183.464,49.381l159.864,276.885    H23.599z"></path>
          <path d="M174.826,136.801v123.893c0,4.773,3.867,8.638,8.638,8.638c4.77,0,8.637-3.863,8.637-8.638V136.801    c0-4.766-3.867-8.637-8.637-8.637C178.693,128.165,174.826,132.036,174.826,136.801z"></path>
          <path d="M183.464,279.393c-5.922,0-10.725,4.8-10.725,10.722s4.803,10.729,10.725,10.729c5.921,0,10.725-4.809,10.725-10.729    C194.189,284.193,189.386,279.393,183.464,279.393z"></path>
         </g>
        </g>
      </svg>
    </div>
    <h2 class="error-title">Something went wrong!</h2>
    <p class="error-message">Some error occured while loading page for you. Please try again.</p>
    <div class="btn-wrap">
      <a href="https://www.hackerrank.com/#" onclick="window.location.reload(true);"><button class="btn-reload">Reload</button></a>
    </div>
  </div>
</div>
<script>
  if(typeof cdnLoaded !== 'undefined' && cdnLoaded === false){
    document.querySelector('.cdn-error-view').style.display = 'block';
  }
</script>

    <script type="text/template" id="navigation">
  <% if(HR.util.showCookieBanner()) { %>
      <div class="cookie-banner-wrapper navigation-banner">
          <div class="cookie-d-flex container">
              <div class="cookie-message msL">We use cookies to ensure you have the best browsing experience on our website.
                  Please read our <a href="/privacy#cookies" target="_blank" class="cookie-link">cookie policy</a> for more information about how we use cookies.
              </div>
              <button class="ui-btn-secondary cookie-accept-btn"><span class="ui-text">Ok</span></button>
          </div>
      </div>
  <% } %>
  <div class="page-header-wrapper theme-m-section">
      <nav class="community-header">
          <div class="container">
              <span class="nav-links theme-m-section"></span>
              <span class="nav-buttons theme-m-section"></span>
          </div>
      </nav>
  </div>
</script>

<script type="text/template" id="nav-links">
  <ul class="nav-links">
      <li class="nav-link-item logo-wrap">
          <a href="/dashboard" class="nav_link backbone logo_mark js_logo_mark logo-link" data-analytics="NavBarLogo"><img id="feed-intro" class="logo-img-small" src="<%- asset_path('brand/logo-new-white-green.svg') %>" alt=""/></a>
      </li>
      <% if (isDashboardV2) { %>
       <li class="nav-link-item">
          <a href="/dashboard" class="nav-link domains" data-analytics="NavBarDomains">
            <span>PREPARE</span>
                  <div class="new-feature-badge">NEW</div>

          </a>
      </li>
      <li class="nav-link-item">
          <a href="/skills-verification" class="nav-link" data-analytics="NavBarCertification">
            <span>CERTIFY</span>
          </a>
      </li>
      <li class="nav-link-item">
          <a href="/contests" class="nav-link contests" data-analytics="NavBarContests">
            <span>COMPETE</span>
          </a>
      </li>
      <% if (isCareerFair) { %>
      <li class="nav-link-item">
              <a href="/career-fair" class="nav-link" data-analytics="NavBarCareerFair" id='vcf-nav-link'>
                  <span>Career Fair</span>
              </a>
          </li>
      <% } %>
      <!-- Disabling Apply/Jobs link on navbar HRC:3967(https://hackerrank.atlassian.net/browse/HRC-3967) -->
      <!-- <li class="nav-link-item">
            <a href="/jobs/search" class="nav-link" data-analytics="NavBarJobs">
                <span>APPLY</span>
                <i class="icon-circle js-jobs-notification navigation-highlight-icon hidden"></i>
            </a>
        </li> -->
       <% } else  { %>
       <li class="nav-link-item">
          <a href="/dashboard" class="nav-link domains" data-analytics="NavBarDomains">
            <span>PRACTICE</span>
          </a>
      </li>
      <li class="nav-link-item">
          <a href="/skills-verification" class="nav-link" data-analytics="NavBarCertification">
            <span>Certification</span>
              <% if (!isCareerFair) { %>
                  <div class="new-feature-badge">NEW</div>
              <% } %>
          </a>
      </li>
      <li class="nav-link-item">
          <a href="/contests" class="nav-link contests" data-analytics="NavBarContests">
            <span>COMPETE</span>
          </a>
      </li>
      <% if (!isCareerFair) { %>
          <!-- <li class="nav-link-item">
              <a href="/jobs/search" class="nav-link" data-analytics="NavBarJobs">
                  <span>JOBS</span>
                  <i class="icon-circle js-jobs-notification navigation-highlight-icon hidden"></i>
              </a>
          </li> -->
          <li class="nav-link-item">
              <a href="/leaderboard" class="nav-link" data-analytics="NavBarLeaderboard" id='leaderboard-nav-link'>
                  <span>LEADERBOARD</span>
              </a>
          </li>
      <% } else { %>
          <li class="nav-link-item">
              <a href="/career-fair" class="nav-link" data-analytics="NavBarCareerFair" id='vcf-nav-link'>
                  <span>Career Fair</span>
                  <div class="new-feature-badge">NEW</div>
              </a>
          </li>
          <li class="dropdown-extra-links">
              <div class="dropdown theme-m-content profile-menu-item extra-menu-item" id="extra-menu">
                  <a class="backbone nav_link dropdown-toggle" href="" data-toggle="dropdown" data-analytics="NavBarFeatureDropDown" title="Expand" aria-label="Expand">
                      <i class="icon-ellipsis"></i>
                  </a>
                  <div class="dropdown-menu drop-list">
                      <ul>
                          <!-- <li class="profile-nav-item"><a class="backbone" href="/jobs/search" data-analytics="NavBarJobs">JOBS</a></li> -->
                          <li class="profile-nav-item"><a class="backbone" href="/leaderboard" data-analytics="NavBarLeaderboard">LEADERBOARD</a></li>
                      </ul>
                  </div>
              </div>
          </li>
      <% } %>
       <% } %>
  </ul>
</script>

<script type="text/template" id="nav-search">
  <div class="hide-in-private-contest search-input input-icon">
      <input type="text" id="search-text" class="new-search-query" autocomplete="off" data-analytics="NavBarSearchBox" placeholder="Search">
      <i class="icon-search"></i>
  </div>
  <div class="hide-in-private-contest search-result hide">
      <ul class="unstyled"></ul>
  </div>
</script>

<script type="text/template" id="nav-buttons">
  <ul class="pull-left psR">
      <li class="hide-in-private-contest search-input-container input-icon main-hr-search" id="search-span">
          <div class="search_form new-search theme-m-content"></div>
      </li>
  </ul>
  <% if (profile && profile.isLoggedIn()) { %>
      <ul class="pull-left nav-wrap mmL">

          <li class="hide-in-private-contest notify_dropdown notify-dropdown dropdown message-dropdown theme-m-content" id="tab-profile-messages">
              <a class="cursor backbone nav_link hr_nav_messages_link" data-toggle="dropdown" data-analytics="NavBarMessageIcon">
                  <i class="icon-theme-m-message icon--single"></i>
                  <span class="indicator number-indicator hr_messages_count hidden"></span>
              </a>
              <div class="dropdown-menu large theme-m-dropdown">
                  <header class="psT psB text-center menu-header">
                      <strong className="header-title">Messages</strong>
                  </header>
                      <div id="notify_messages" class="dropdown-body">
                          <ul></ul>
                      </div>
                  <footer class="final text-center show-all">
                      <a class="btn backbone show-all-link" href="/inbox" data-analytics="NavBarMessageShowAll">Show All</a>
                  </footer>
              </div>
          </li>
          <li class="dropdown notify_dropdown theme-m-content" id="tab-profile-notifs">
              <a class="cursor backbone nav_link hr_nav_notifications_link" data-toggle="dropdown" data-analytics="NavBarNotificationsIcon">
                  <i class="icon-theme-m-notification icon--single"></i>
                  <span class="indicator number-indicator hr_notifications_count hidden"></span>
              </a>
              <div class="dropdown-menu large theme-m-dropdown" id="notify_broadcasts">
                  <header class="psA">
                      <strong>Notifications</strong>
                      <a class="hr_archive_all archive pull-right" data-analytics="NavBarNotificationsArchiveAll"><i class="icon-folder-open"></i>Archive All</a>
                  </header>
                  <div class="clearfix dropdown-body">
                      <ul class="hr_nav_notifications_list">
                      </ul>
                  </div>
                  <footer class="final text-center show-all">
                      <a class="btn backbone show-all-link" href="/notifications" data-analytics="NavBarNotificationsShowAll">Show All</a>
                  </footer>
              </div>
          </li>
          <li class="dropdown-auth">
              <div class="dropdown theme-m-content profile-menu-item" id="profile-menu">
                  <a class="backbone nav_link dropdown-toggle" href="" data-toggle="dropdown" data-analytics="NavBarProfileDropDown">
                      <img src="<%= _profile.avatar %>" alt="" class="avatar" onerror="this.onerror=null; this.src='https://d1ce3iv5vajdy.cloudfront.net/hackerrank/assets/gravatar.jpg';">
                      <span class="mmR profile-username"><%- _profile.username %></span>
                      <i class="icon-down-open"></i>
                  </a>
                  <div class="dropdown-menu drop-list pull-right">
                      <ul>
                          <li class="hide-in-private-contest profile-nav-item"><a class="navigation_hackos hackos-count backbone" href="/<%- _profile.username %>/hackos" data-analytics="NavBarProfileDropDownHackos">Hackos: <span class="navigation_hackos-count"><%= _profile.hacko_amount %></span></a></li>
                          <li class="hide-in-private-contest profile-nav-item">
                              <a class="backbone" rel="tooltip" data-placement="left" href="/<%- _profile.username %>" data-analytics="NavBarProfileDropDownProfile">
                                  Profile
                                  <!-- NOTE also add title="x% complete" to profile link-->
                                  <div class="ui-progress-bar theme-progress-bar">
                                      <div class="progress-filler" style="width: <%= _profileProgress %>%;"></div>
                                  </div>
                              </a>
                          </li>
                          <% if (_profile.show_dashboard_v2) { %>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="/leaderboard" data-analytics="NavBarProfileDropDownALeaderboard">Leaderboard</a></li>
                           <% } %>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="/settings" data-analytics="NavBarProfileDropDownSettings">Settings</a></li>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="/challenges/bookmarks" data-analytics="NavBarDropDownBookmarks">Bookmarks</a></li>
                          <% if (HR.ABTest && HR.ABTest.is_variant("hrc-code-snippets", "trm1")){ %>
                              <li class="hide-in-private-contest profile-nav-item"><a href="/snippets" data-analytics="NavBarProfileDropDownCodeSnippets">Code Snippets</a></li>
                          <% } %>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="/network" data-analytics="NavBarProfileDropDownNetwork">Network</a></li>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="/submissions" data-analytics="NavBarProfileDropDownSubmissions">Submissions</a></li>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="/administration" data-analytics="NavBarProfileDropDownAdministration">Administration</a></li>
                          <li class="profile-nav-item"><a class="logout-button" data-analytics="NavBarProfileDropDownLogout">Logout</a></li>
                      </ul>
                  </div>
              </div>
          </li>
      </ul>
  <% } %>
</script>

    <script type="text/template" id="breadcrumb">
    <% var counter = 0; %>
    <div class="content-header">
        <div class="container">
            <div class="clearfix">
                <ol itemscope itemtype="http://schema.org/BreadcrumbList" class="pull-left mdT msB pjT bcrumb">
                    <% var breadcrumb_level = 0; var levelValKeys = _.keys(level_values);%>
                    <% for (var index in level_values) { %>
                      <li itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
                        <% if (counter==0) {
                             counter = counter + 1;
                           } else { %>
                             <i class="icon-right-open mmL"></i>
                        <% } %>
                        <a itemprop="item" href="<%= level_values[index].url %>" class="backbone"
                           data-analytics="Breadcrumb" data-attr1="<%- level_values[index].text %>"
                           data-attr2="<%= index %>" data-attr7="<%= breadcrumb_level += 1 %>"><span itemprop="name"><%- level_values[index].text %></span></a>
                        <meta itemprop="position" content="<%- breadcrumb_level %>" />
                      </li>
                    <% } %>
                </ol>
                 <div class="pull-right hide domain-scores">
                    <div class="pull-left badge-progress">
                    </div>
                    <div class="pull-right pdT brcumb-points">
                        <span class="zeta bold">Points: </span><span class="bold domain-score"></span>
                        <span class="domain-rank-span">
                            <span class="zeta bold">Rank: </span><span class="bold msR domain-rank "></span>
                        </span>
                    </div>
                 </div>
                <div class="social-share-wrap-2 hide"></div>
            </div>
        </div>
    </div>
</script>


    <div id="wrapper" class="theme-m-content" style="min-height: 624px;">
        <div id="navigation">
  
  <div class="page-header-wrapper theme-m-section">
      <nav class="community-header">
          <div class="container">
              <span class="nav-links theme-m-section">
  <ul class="nav-links">
      <li class="nav-link-item logo-wrap">
          <a href="https://www.hackerrank.com/dashboard?h_r=logo" class="nav_link backbone logo_mark js_logo_mark logo-link" data-analytics="NavBarLogo"><img id="feed-intro" class="logo-img-small" src="./product_files/logo-new-white-green-ff31cc27c3f5b38c15b7b1d7b6b2a672968c17fb25e1d654abcf0378e0925688.svg" alt=""></a>
      </li>
      
       <li class="nav-link-item">
          <a href="https://www.hackerrank.com/dashboard" class="nav-link domains" data-analytics="NavBarDomains">
            <span>PREPARE</span>
                  <div class="new-feature-badge">NEW</div>

          </a>
      </li>
      <li class="nav-link-item">
          <a href="https://www.hackerrank.com/skills-verification" class="nav-link" data-analytics="NavBarCertification">
            <span>CERTIFY</span>
          </a>
      </li>
      <li class="nav-link-item">
          <a href="https://www.hackerrank.com/contests" class="nav-link contests active" data-analytics="NavBarContests">
            <span>COMPETE</span>
          </a>
      </li>
      
      <!-- Disabling Apply/Jobs link on navbar HRC:3967(https://hackerrank.atlassian.net/browse/HRC-3967) -->
      <!-- <li class="nav-link-item">
            <a href="/jobs/search" class="nav-link" data-analytics="NavBarJobs">
                <span>APPLY</span>
                <i class="icon-circle js-jobs-notification navigation-highlight-icon hidden"></i>
            </a>
        </li> -->
       
  </ul>
</span>
              <span class="nav-buttons theme-m-section">
  <ul class="pull-left psR">
      <li class="hide-in-private-contest search-input-container input-icon main-hr-search" id="search-span">
          <div class="search_form new-search theme-m-content">
  <div class="hide-in-private-contest search-input input-icon">
      <input type="text" id="search-text" class="new-search-query ui-autocomplete-input" autocomplete="off" data-analytics="NavBarSearchBox" placeholder="Search" fdprocessedid="h84wi">
      <i class="icon-search"></i>
  </div>
  <div class="hide-in-private-contest search-result hide" style="display: block;">
      <ul class="unstyled"></ul>
  </div>
</div>
      </li>
  </ul>
  
      <ul class="pull-left nav-wrap mmL">

          <li class="hide-in-private-contest notify_dropdown notify-dropdown dropdown message-dropdown theme-m-content" id="tab-profile-messages">
              <a class="cursor backbone nav_link hr_nav_messages_link" data-toggle="dropdown" data-analytics="NavBarMessageIcon">
                  <i class="icon-theme-m-message icon--single"></i>
                  <span class="indicator number-indicator hr_messages_count hidden"></span>
              </a>
              <div class="dropdown-menu large theme-m-dropdown">
                  <header class="psT psB text-center menu-header">
                      <strong classname="header-title">Messages</strong>
                  </header>
                      <div id="notify_messages" class="dropdown-body">
                          <ul></ul>
                      </div>
                  <footer class="final text-center show-all">
                      <a class="btn backbone show-all-link" href="https://www.hackerrank.com/inbox" data-analytics="NavBarMessageShowAll">Show All</a>
                  </footer>
              </div>
          </li>
          <li class="dropdown notify_dropdown theme-m-content" id="tab-profile-notifs">
              <a class="cursor backbone nav_link hr_nav_notifications_link" data-toggle="dropdown" data-analytics="NavBarNotificationsIcon">
                  <i class="icon-theme-m-notification icon--single"></i>
                  <span class="indicator number-indicator hr_notifications_count">2</span>
              </a>
              <div class="dropdown-menu large theme-m-dropdown" id="notify_broadcasts">
                  <header class="psA">
                      <strong>Notifications</strong>
                      <a class="hr_archive_all archive pull-right" data-analytics="NavBarNotificationsArchiveAll"><i class="icon-folder-open"></i>Archive All</a>
                  </header>
                  <div class="clearfix dropdown-body">
                      <ul class="hr_nav_notifications_list">
                      </ul>
                  </div>
                  <footer class="final text-center show-all">
                      <a class="btn backbone show-all-link" href="https://www.hackerrank.com/notifications" data-analytics="NavBarNotificationsShowAll">Show All</a>
                  </footer>
              </div>
          </li>
          <li class="dropdown-auth">
              <div class="dropdown theme-m-content profile-menu-item" id="profile-menu">
                  <a class="backbone nav_link dropdown-toggle" href="https://www.hackerrank.com/" data-toggle="dropdown" data-analytics="NavBarProfileDropDown">
                      <img src="./product_files/gravatar.jpg" alt="" class="avatar" onerror="this.onerror=null; this.src=&#39;https://d1ce3iv5vajdy.cloudfront.net/hackerrank/assets/gravatar.jpg&#39;;">
                      <span class="mmR profile-username">yashasvinitripa1</span>
                      <i class="icon-down-open"></i>
                  </a>
                  <div class="dropdown-menu drop-list pull-right">
                      <ul>
                          <li class="hide-in-private-contest profile-nav-item"><a class="navigation_hackos hackos-count backbone" href="https://www.hackerrank.com/yashasvinitripa1/hackos" data-analytics="NavBarProfileDropDownHackos">Hackos: <span class="navigation_hackos-count">224</span></a></li>
                          <li class="hide-in-private-contest profile-nav-item">
                              <a class="backbone" rel="tooltip" data-placement="left" href="https://www.hackerrank.com/yashasvinitripa1" data-analytics="NavBarProfileDropDownProfile">
                                  Profile
                                  <!-- NOTE also add title="x% complete" to profile link-->
                                  <div class="ui-progress-bar theme-progress-bar">
                                      <div class="progress-filler" style="width: 30%;"></div>
                                  </div>
                              </a>
                          </li>
                          
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="https://www.hackerrank.com/leaderboard" data-analytics="NavBarProfileDropDownALeaderboard">Leaderboard</a></li>
                           
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="https://www.hackerrank.com/settings" data-analytics="NavBarProfileDropDownSettings">Settings</a></li>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="https://www.hackerrank.com/challenges/bookmarks" data-analytics="NavBarDropDownBookmarks">Bookmarks</a></li>
                          
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="https://www.hackerrank.com/network" data-analytics="NavBarProfileDropDownNetwork">Network</a></li>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="https://www.hackerrank.com/submissions" data-analytics="NavBarProfileDropDownSubmissions">Submissions</a></li>
                          <li class="hide-in-private-contest profile-nav-item"><a class="backbone" href="https://www.hackerrank.com/administration" data-analytics="NavBarProfileDropDownAdministration">Administration</a></li>
                          <li class="profile-nav-item"><a class="logout-button" data-analytics="NavBarProfileDropDownLogout">Logout</a></li>
                      </ul>
                  </div>
              </div>
          </li>
      </ul>
  
</span>
          </div>
      </nav>
  </div>
</div>
        <div id="side-navigation"></div>
        <div id="verifyaccount" style="display: none;">
<div class="verify-wrapper">
  <div class="container">
    <div class="verify-content">
      <div class="verify-message">
        The email address you signed up with has not been verified. You won't be ranked on the leaderboard until you verify your account.
      </div>
      <button class="ui-btn ui-btn-normal resend-btn send-verification" tabindex="0">
        <div class="ui-content align-icon-right">
          <span class="ui-text">
            
              SEND AGAIN
            
          </span>
        </div>
      </button>
      <i class="close close-verification icon--single icon2-close"></i>
    </div>
  </div>
</div>

</div>
        <div id="ajax-msg-wrap"><div id="ajax-msg" style="margin-left: -0.2px; display: none;"><span class="ajax-loader"></span><span class="ajax-msg"></span></div></div>
        <!--<div id="countdowntimer" style="display: none;"></div>-->
        <div id="breadcrumb" style="display: block;">
    
    <div class="content-header">
        <div class="container">
            <div class="clearfix">
                <ol itemscope="" itemtype="http://schema.org/BreadcrumbList" class="pull-left mdT msB pjT bcrumb">
                    
                    
                      <li itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
                        
                        <a itemprop="item" href="https://www.hackerrank.com/contests" class="backbone" data-analytics="Breadcrumb" data-attr1="All Contests" data-attr2="global" data-attr7="1"><span itemprop="name">All Contests</span></a>
                        <meta itemprop="position" content="1">
                      </li>
                    
                      <li itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
                        
                             <i class="icon-right-open mmL"></i>
                        
                        <a itemprop="item" href="https://www.hackerrank.com/contests/t1-aiml2023/challenges" class="backbone" data-analytics="Breadcrumb" data-attr1="T1_aiml2023" data-attr2="contest" data-attr7="2"><span itemprop="name">T1_aiml2023</span></a>
                        <meta itemprop="position" content="2">
                      </li>
                    
                      <li itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
                        
                             <i class="icon-right-open mmL"></i>
                        
                        <a itemprop="item" href="https://www.hackerrank.com/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1" class="backbone" data-analytics="Breadcrumb" data-attr1="Vowel or Consonant 1" data-attr2="challenge" data-attr7="3"><span itemprop="name">Vowel or Consonant 1</span></a>
                        <meta itemprop="position" content="3">
                      </li>
                    
                </ol>
                 <div class="pull-right hide domain-scores" style="display: none;">
                    <div class="pull-left badge-progress">
                    </div>
                    <div class="pull-right pdT brcumb-points">
                        <span class="zeta bold">Points: </span><span class="bold domain-score"></span>
                        <span class="domain-rank-span">
                            <span class="zeta bold">Rank: </span><span class="bold msR domain-rank "></span>
                        </span>
                    </div>
                 </div>
                <div class="social-share-wrap-2 hide"></div>
            </div>
        </div>
    </div>
</div>
        <div id="flash"></div>
        <div id="followbanner"></div>
        <div id="submission-success-messages"></div>
        <div id="contestwide-broadcast"></div>
        <div id="content" class="main_content"><div class="challenge-view"><div>
   
    <div class="challenge-header"><div class="container">
    <div class="mdT mmB span10">
        <div class="clearfix">
            <h2 class="hr_tour-challenge-name pull-left mlT">
                Vowel or Consonant 1
                
                
            </h2>
            
            
            </div>
        </div>
        
    </div>

            

<div class="container">
    <ul class="nav-tabs nav mlT">

        <!-- Problem -->
        <li id="problemTab" class="active">
            <a class="hr-problem-link" href="https://www.hackerrank.com/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1" data-analytics="ChallengeViewTab" data-attr1="vowel-or-consonant-1-1" data-attr2="Problem">Problem</a>
        </li>

        <!-- Expert (Live) -->
        

        <!-- Submissions -->
        
            <li id="submissionsTab">
                <a class="hr-submissions-link" href="https://www.hackerrank.com/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1/submissions" data-analytics="ChallengeViewTab" data-attr1="vowel-or-consonant-1-1" data-attr2="Submissions">Submissions</a>
            </li>
        

        <!-- Leadeboard -->
        
            <li id="leaderboardTab">
                <a class="hr-leaderboard-link" href="https://www.hackerrank.com/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1/leaderboard" data-analytics="ChallengeViewTab" data-attr1="vowel-or-consonant-1-1" data-attr2="Leaderboard">Leaderboard</a>
            </li>
        

        <!-- Discussion -->
        
            <li id="forumTab">
                <a class="hr-forum-link" href="https://www.hackerrank.com/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1/forum" data-analytics="ChallengeViewTab" data-attr1="vowel-or-consonant-1-1" data-attr2="Discussions">Discussions</a>
            </li>
        

        <!-- Editorial -->
        

        <!-- Custom Pages -->
        

        <!-- Topics -->
        
    </ul>
</div>
</div>
    <style></style>
    <section class="challenge-interface">
        <div class="challenge-body">
          <div class="challenge-container-element hidden challenge-container-elements-loading">
            <div class="gray block-center">
              <div style="background: url(https://hrcdn.net/hackerrank/assets/hackerrank_spinner_64x64-51ddd3e4a3bcc9860b57777c53e0d4305e9f727eb5a46deb2afd112a7df18222.gif); height: 64px; width: 64px; display: inline-block;"></div>
            </div>
          </div>
        <div class="challenge-body-elements-problem challenge-container-element"><div class="challenge-content"><div class="container fs-container">
    <div class="row">
        <div class="span-sm-11 hr_tour-problem-statement problem-statement">
            
            
            
            
            <div class="content-text challenge-text mlB">
                <div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>This program will read a character from user and check whether it is VOWEL or CONSONANT if entered character was an alphabet using conditional opertors statement.</p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ol>
<li>Take a char ch fom the user.</li>
</ol></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ol>
<li>If other than alphabet is entered then print "Not an alphabet."</li>
</ol></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ol>
<li>If entered character is vowel then print "Vowel."</li>
<li>If entered character is consonant then print "Consonant."</li>
<li>If entered character is not alphabet then print "Not an alphabet.."</li>
</ol></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 0</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span class="err">e</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 0</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">Vowel.</span>
</pre></div>
</div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 1</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">X</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 1</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">Consonant.</span>
</pre></div>
</div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 2</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span class="err">2</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 2</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><style id="MathJax_SVG_styles">.MathJax_SVG_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax_SVG .MJX-monospace {font-family: monospace}
.MathJax_SVG .MJX-sans-serif {font-family: sans-serif}
.MathJax_SVG {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax_SVG * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.mjx-svg-href {fill: blue; stroke: blue}
.MathJax_SVG_LineBox {display: table!important}
.MathJax_SVG_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
</style><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">Not an alphabet.</span>
</pre></div>
</div></div></div>
            </div>
            

            
        </div>

        <aside class="span-sm-4 pull-right fullscreen-hide challenge-sidebar">
            <div class="challenge-sidebar-container">

<div class="social-share-wrap-2"><div class="social-share-view-2 social-buttons plR mlB pull-left full-width">
  <a class="social-btn cursor facebook-share-btn msL inline-block txt-white">
    <i class="icon-facebook"></i>
  </a>

  <a class="social-btn cursor twitter-share-btn msL inline-block txt-white txt-white">
    <i class="icon-twitter"></i>
  </a>

  <a class="social-btn cursor linkedin-share-btn msL inline-block txt-white">
    <i class="icon-linkedin"></i>
  </a>
</div>
</div>

<span class="header_countdowntimer"></span>

<div class="countdowntimer">
<span class="contest-status ">
    <small>
        
            <span class="timer-color-running">
                 
                
                    
                        Contest ends in
                        <abbr class="countdown timeago endtime cursor contest-countdown" style="border-bottom: 1px dotted black;" data-original-title="" title="">a month</abbr>
                    
                
            </span>
        
    </small>
</span>
</div>





<div class="sidebar_problem_difficulty">


    <p class="bold zeta">Submissions:</p>
    
    <a href="https://www.hackerrank.com/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1/leaderboard" data-analytics="ChallengeViewHackerCount" data-attr1="vowel-or-consonant-1-1">297</a>
    


    <div>
        <p class="bold zeta">Max Score:</p>
            <p class="sidebar_att">
            
            10
            
            </p>
    </div>


    <div>
        
          <p class="bold zeta">Difficulty: </p>
          <p class="sidebar_att">
              
                  Easy
              
          </p>
        
    </div>


</div>

<div class="challenge-rating rating">
  <p class="bold zeta">Rate This Challenge: </p>
  
    <i class="icon--single icon-star-empty cursor" data-analytics="RatedChallenge" data-attr7="1"></i>
  
    <i class="icon--single icon-star-empty cursor" data-analytics="RatedChallenge" data-attr7="2"></i>
  
    <i class="icon--single icon-star-empty cursor" data-analytics="RatedChallenge" data-attr7="3"></i>
  
    <i class="icon--single icon-star-empty cursor" data-analytics="RatedChallenge" data-attr7="4"></i>
  
    <i class="icon--single icon-star-empty cursor" data-analytics="RatedChallenge" data-attr7="5"></i>
  
  <span class="rating_reply color-alt-grey hidden psL">Thanks!</span>
  <div class="rating_feedback hidden">
    <p class="small color-alt-grey msT">How can we improve?</p>
    <button class="btn btn-standard bb-rate-challenge msT" data-analytics="RatingFeedback">Let us know</button>
  </div>
</div>






<div id="sidebar-more-options" class="hide">
  <div class="mlB mlT">
      <a class="challenge-sidebar-anchor pointer" href="https://www.hackerrank.com/rest/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1/download_pdf?language=English" target="_blank" id="pdf-link" data-analytics="ChallengeViewSidebarPDF" data-attr1="vowel-or-consonant-1-1" style="color:#979faf;"><i class="icon-download"></i>Download problem statement</a>
  </div>
  <div class="mlB">
    <a class="challenge-sidebar-anchor pointer" href="https://www.hackerrank.com/rest/contests/t1-aiml2023/challenges/vowel-or-consonant-1-1/download_testcases" target="_blank" id="test-cases-link" data-analytics="ChallengeViewSidebarTestCases" data-attr1="vowel-or-consonant-1-1" style="color:#979faf;"><i class="icon-download"></i>
      
        Download sample test cases
      
    </a>
  </div>
  <div class="fullscreen-hide">
      <a href="https://www.hackerrank.com/#" class="challenge-sidebar-anchor js-suggest-edits challenge_suggestion-toggle fullscreen-hide" data-analytics="ChallengeViewSuggestEdit" data-attr1="vowel-or-consonant-1-1" style="color:#979faf;"><i class="icon-edit"></i>Suggest Edits</a>

      <div class="challenge_suggestion fullscreen-hide row">
          <div class="span16">
              <div class="formgroup text-center">
                  <div class="alert error hide"></div>
                  <div class="alert success hide">Suggestion Sent!</div>
              </div>
              <form id="suggestion-form" class="hide challenge_suggestion-form fullscreen-hide" __bizdiag="-1696069907" __biza="WJ__">
                  <p class="challenge_suggestion-header pdB">Thanks for helping us refine this problem statement. Please address your suggestions below. </p>
                  <textarea id="suggestion" rows="10" width="100" class="tall challenge_suggestion-input"></textarea>
                  <div class="challenge_suggestion-buttons access-buttons clearfix">
                      <div class="pull-right mlB">
                          <button class="btn btn-green js-suggestion-save pull-right" data-analytics="Submit Suggestion">Submit Suggestion</button>
                          <button class="btn btn-text js-suggestion-cancel pull-right" data-analytics="Cancel Suggestion">Cancel</button>
                      </div>
                  </div>
              </form>
          </div>
      </div>
  </div>
  <div class="language-selector pmT">
    
    <div class="psT hide small color-alt-grey" id="preference-msg">
    <a class="language-preference btn btn-small msB" href="https://www.hackerrank.com/#">Set as default</a><br>
    <p class="mjB">You can always change back later.</p>
    </div>
  </div>
</div>
<div class="msB"><a id="sidebar-more-button" class="challenge-sidebar-anchor pointer">More</a></div>




</div></aside>
    </div>
</div>
</div><div class="challenge-request"><div class="challenge-input codeeditor-wrapper container fs-container mlB"><div id="codeshell-wrapper">
<div class="clearfix grey-header fixed-hand0 cap plL plR psT psB" style="position: relative;">
  <div class="msT pull-left"><em id="status-text"></em></div>
  
  
  <div class="pull-right">
    
    <div class="inline large lines inverse pull-right msT msL">
      
      
      <a class="restorefullscreen force-hide active-link no-select">
          <i class="icon-resize-small-alt icon--grey no-select"></i></a>
      <a class="fullscreen active-link no-select" data-analytics="Switch to fullscreen"><i class="icon-resize-full-alt icon--grey no-select"></i></a>
      
      
      
      <a class="hide" style="display:none;"></a>
      <div class="settings-editor" style="position:relative; margin-left: 0px;">
        <a class="cursor no-select" data-analytics="CodeShellShowPreferences" id="show-preferences"><i class="icon-cog icon--grey no-select"></i></a>
        <div id="pref-pane" style="position: absolute;right: -0.5em;top: 2em;z-index: 9;background: #fff;border: 1px solid #ddd;border-radius: 5px;padding: 10px;  width: 25em; display: none;">
          <div style="position: absolute;width: 0;right: 0.8em;height: 0;border-left: 7px solid transparent;border-right: 7px solid transparent;border-bottom: 7px solid #ddd;top: -0.4em;"></div>
          
            <div class="formgroup horizontal">
              <label class="span5">Editor Mode</label>
              <div class="inline">
                <div class="btn-group no-select">
                  <a data-analytics="CodeShellEditorMode" data-attr1="Emacs" class="cursor emacs btn btn-small btn-white editor-mode-button no-select" data-editor="emacs">Emacs</a>
                  <a data-analytics="CodeShellEditorMode" data-attr1="Normal" class="cursor default btn btn-small btn-white editor-mode-button no-select btn-primary" data-editor="sublime">Normal</a>
                  <a data-analytics="CodeShellEditorMode" data-attr1="Vim" class="cursor vim btn btn-small btn-white editor-mode-button no-select" data-editor="vim">Vim</a>
                </div>
              </div>
            </div>
          
          
            <div class="formgroup horizontal">
              <label class="span5">Editor Theme</label>
              <div class="inline">
                <div class="btn-group no-select">
                  <a data-analytics="CodeShellEditorTheme" data-attr1="Light" class="cursor light btn btn-small btn-white editor-theme-button no-select btn-primary" data-editor="light">Light</a>
                  <a data-analytics="CodeShellEditorTheme" data-attr1="Dark" class="cursor dark btn btn-small btn-white editor-theme-button no-select" data-editor="dark">Dark</a>
                </div>
              </div>
            </div>
          
          <div class="formgroup horizontal">
            <label class="span5">Tab Spaces</label>
            <div class="inline">
              <div class="btn-group no-select">
                <a data-analytics="CodeShellEditorSpace" data-attr1="2" class="cursor 2space btn btn-small btn-white editor-tabspace-button no-select" data-editor="2">2 spaces</a>
                <a data-analytics="CodeShellEditorSpace" data-attr1="4" class="cursor 4space  btn btn-small btn-white editor-tabspace-button no-select btn-primary" data-editor="4">4 spaces</a>
                <a data-analytics="CodeShellEditorSpace" data-attr1="8" class="cursor 8space btn btn-small btn-white editor-tabspace-button no-select" data-editor="8">8 spaces</a>
              </div>
            </div>
          </div>
          
            <div class="formgroup horizontal">
              <label class="span5">Intellisense
              
              <span class="js-tooltip" data-toggle="tooltip" data-placement="bottom" title="Available only for C, C++, Java, Python, JavaScript, Ruby, PHP, C# and Go" data-attr1="CodeCompletion">
              
              <i class="icon-info-circled fnt-sz-small txt-navy"></i>
              </span></label>
              <div class="inline">
                <div class="btn-group no-select">
                  <a data-analytics="CodeShellAutoComplete" data-attr1="Enable" class="cursor emacs btn btn-small btn-white editor-autocomplete-button no-select btn-primary" data-editor="true">Enable</a>
                  <a data-analytics="CodeShellAutoComplete" data-attr1="Disable" class="cursor default btn btn-small btn-white editor-autocomplete-button no-select" data-editor="false">Disable</a>
                </div>
              </div>
            </div>
          
          
        </div>
      </div>
      
    </div>
    
    <div class="pull-right lang-placeholder">
      <div class="dummy-lang-container hide"></div>
      <div class="select2-container" id="s2id_select-lang"><a href="javascript:void(0)" onclick="return false;" class="select2-choice" tabindex="-1">   <span>Python 3</span><abbr class="select2-search-choice-close"></abbr>   <div><b></b></div></a><input class="select2-focusser select2-offscreen" type="text" id="s2id_autogen28" fdprocessedid="itg60b"><div class="select2-drop select2-display-none">   <div class="select2-search select2-search-hidden select2-offscreen">       <input type="text" autocomplete="off" autocorrect="off" autocapitilize="off" spellcheck="false" class="select2-input">   </div>   <ul class="select2-results">   </ul></div></div><input type="hidden" id="select-lang" tabindex="-1" class="select2-offscreen" value="python3">
    </div>
    
    <div class="clearfix"></div>
  </div>
</div>

<div class="hr_tour-code-solution movable-hand flex-row" style="display: flex;">
  
  <div class="code-checker">
    <div id="notification-message" class="clearfix grey-header cap  hidden "> </div>
    <div class="code-editors">
      
       <div class="loading-mode" style="display: none;">Loading Editor... </div> 
      <div class="code-body" style="display: block;">
        
       <textarea id="codeview" style="width: 100%; display: none;"></textarea><div class="CodeMirror CodeMirror-wrap cm-s-default"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 4.79993px; left: 59.8px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 55px; margin-bottom: -16px; border-right-width: 14px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre><div class="CodeMirror-linenumber CodeMirror-gutter-elt"><div>1</div></div></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 20.275px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: -55px; width: 55px;"></div><div class="CodeMirror-gutter-wrapper CodeMirror-activeline-gutter" style="left: -55px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 16px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div></div><div style="position: absolute; height: 14px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="height: 42px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-lint-markers"></div><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 29px;"></div><div class="CodeMirror-gutter CodeMirror-foldgutter"></div></div></div></div>
       </div>
      
      <div class="clearfix"></div>
    </div>
    <div id="codeeditor-statusbar" class="clearfix psA codeeditor_statusbar">
      <span id="statusbar-mode"></span>
      <div class="pull-right">
        <span id="statusbar-line"></span>
        <span id="statusbar-col"></span>
        <span id="statusbar-count"></span>
      </div>
    </div>
  </div>
</div><div class="clearfix pmR pmL pmB plT fixed-hand1 codeshell-footer">
  <div class="pull-right">
    
    
    <button class="btn bb-compile msR " data-analytics="Compile and Test" fdprocessedid="bj27vh">Run Code</button>
    
    
    <button class="btn btn-primary bb-submit ans-submit" data-analytics="Submit Code" fdprocessedid="87f8pc">Submit Code</button>
    
    
  </div>
  <div class="pull-left inline">
      
      <button class="btn btn-text upload_file mlR" data-analytics="Upload File" type="button" fdprocessedid="c83vfd"><i class="icon-upload"></i>Upload Code as File</button>
      
      
      
      <div class="mmT">
          <label for="customtestcase"><div class="custom-checkbox-v3"><input type="checkbox" id="customtestcase"><span></span></div><span class="lmT msL">Test against custom input</span></label>
          
          <textarea rows="5" id="custominput" style="display:none"></textarea>
          
      </div>
      
  </div>
  
</div></div><div id="submission-message"></div></div>
</div><div class="challenge-response container fs-container"><h5 class="output-progress padded light-wrap hide mlT mlB psT" style="padding-top: 100px; padding-bottom: 100px; text-align: center;"></h5>
<div class="output-area-wrap hide">
  <div class="output-area mlT psT hide" id="output-area"></div>
</div></div><div class="challenge-copyright"></div></div></div>
    </section>
</div>
</div></div>
        <div id="hacker"></div>
    </div>
    <div id="autocomplete-container" style="position:absolute; width: 330px; z-index: 2000; padding-top: 1px;"><ul class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content theme-m-content" id="ui-id-301" tabindex="0" style="display: none;"></ul></div>
    <footer class="page_footer">
    <div>
        <div class="text-center">
            <p style="font-size: 14px; margin-top: 5px; margin-bottom: 0px;">
              <span class="internal-links">
                <a target="_blank" href="https://www.hackerrank.com/interview/interview-preparation-kit?utm_source=website&amp;utm_medium=footer&amp;utm_campaign=website" class="interview-prep" data-analytics="FooterLinkCalendar">Interview Prep</a>
                |
                <a target="_blank" href="https://blog.hackerrank.com/" class="blog" data-analytics="FooterLinkBlog">Blog</a>
                |
                <a target="_blank" href="https://www.hackerrank.com/scoring" class="scoring" data-analytics="FooterLinkScoring">Scoring</a>
                |
                <a target="_blank" href="https://www.hackerrank.com/environment" class="environment" data-analytics="FooterLinkEnvironment">Environment</a>
                |
                <a target="_blank" href="https://www.hackerrank.com/faq" class="faq" data-analytics="FooterLinkFAQ">FAQ</a>
                |
              </span>
              <a target="_blank" href="https://www.hackerrank.com/aboutus" data-analytics="FooterLinkAboutUs">About Us</a>
              |
              <a target="_blank" href="https://www.hackerrank.com/support" data-analytics="FooterLinkSupport">Support</a>
              |
              <a target="_blank" href="https://www.hackerrank.com/careers" data-analytics="FooterLinkCareers">Careers</a>
              |
              <a target="_blank" href="https://www.hackerrank.com/terms-of-service" data-analytics="FooterLinkTermsOfService">Terms Of Service</a>
              |
              <a target="_blank" href="https://www.hackerrank.com/privacy" data-analytics="FooterLinkPrivacyPolicy">Privacy Policy</a>
              |
            </p>
        </div>
    </div>
</footer>

    <ol id="hr_tour-intro-tour" class="hide">
        <li data-class="hr_tour-challenge-name" data-options="tipLocation:bottom"><h5 class="walkthrough-header">Challenge Walkthrough</h5><span class="walkthrough-text">Let's walk through this sample challenge and explore the features of the code editor.</span><span class="walkthrough-progress">1 of 6</span></li>
        <li data-class="hr_tour-problem-statement" data-options="tipLocation:top"><h5 class="walkthrough-header">Review the problem statement</h5><span class="walkthrough-text">Each challenge has a problem statement that includes sample inputs and outputs. Some challenges include additional information to help you out.</span><span class="walkthrough-progress">2 of 6</span></li>
        <li data-class="hr_tour-select-language" data-options="tipLocation:left"><h5 class="walkthrough-header">Choose a language</h5><span class="walkthrough-text">Select the language you wish to use to solve this challenge.</span><span class="walkthrough-progress">3 of 6</span></li>
        <li data-class="hr_tour-code-solution" data-options="tipLocation:top"><h5 class="walkthrough-header">Enter your code</h5><span class="walkthrough-text">Code your solution in our custom editor or code in your own environment and upload your solution as a file.</span><span class="walkthrough-progress">4 of 6</span></li>
        <li data-class="hr_tour-compile-test" data-options="tipLocation:left"><h5 class="walkthrough-header">Test your code</h5><span class="walkthrough-text">You can compile your code and test it for errors and accuracy before submitting.</span><span class="walkthrough-progress">5 of 6</span></li>
        <li data-class="hr_tour-submit-code" data-button="Done" data-options="tipLocation:left"><h5 class="walkthrough-header">Submit to see results</h5><span class="walkthrough-text">When you're ready, submit your solution! Remember, you can go back and refine your code anytime.</span><span class="walkthrough-progress">6 of 6</span></li>
    </ol>
    <ol id="hr_tour-intro-part-2-tour" class="hide">
        <li data-class="hr_tour-leaderboard">Check your score</li>
    </ol>
    <script type="text/javascript">
     // disable forum social interaction
     HR.disable_fsi = false;
    </script>

    <script type="text/javascript">
      // Setting up jobs constants for use in frontend
      // Jobs visa constants - visa's accepted by company
      HR.VISA_TYPE_NONE = 0
      HR.VISA_TYPE_ALL = 1
      HR.VISA_TYPE_US_RESIDENT = 2
    </script>

    <script type="text/javascript">
      HR.REACT_ROUTE_CONFIG = {
  "var1": [],
  "var2": [],
  "complete": [
    "^/domains/?.*$",
    "^/dashboard/?(\\?.*|$)",
    "^/interview((/|\\?).*|$)",
    "^/contests/((projecteuler)|(hourrank-[0-9]+))(/(?!(judge/)?submissions).*)?$",
    "^/contests/?((archived|college)(/\\d*)?)?/?(\\?.*|$)",
    "^/terms-of-service/?(\\?.*|$)",
    "^/faq-hacker-level/?(\\?.*|$)",
    "^/privacy/?(\\?.*|$)",
    "^/leaderboard((/|\\?).*|$)",
    "^/skills-verification((/|\\?).*|$)",
    "^/settings/email-preferences((/|\\?).*|$)",
    "^/settings/language((/|\\?).*|$)",
    "^/settings/change-password((/|\\?).*|$)",
    "^/settings/shipping-details((/|\\?).*|$)",
    "^/settings/personalization((/|\\?).*|$)",
    "^/work/login($|\\?|/).*",
    "^/work/tests((/|\\?).*|$)",
    "^/work/settings((/|\\?).*|$)",
    "^/work/settings/data-manager((/|\\?).*|$)",
    "^/jobs/search/?(\\?.*|$)",
    "^/jobs/dashboard/.+$",
    "^/environment(/?.*|$)",
    "^/work/library((/|\\?).*|$)",
    "^/work/projects((/|\\?).*|$)",
    "^/work/teams((/|\\?).*|$)",
    "^/calendar/?(\\?.*|$)",
    "^/snippets((/.*)|(\\?.*)|$)",
    "^/feed/?(\\?.*|$)",
    "^/challenges/([^/]+?)(?!/(topics))((/?\\?.*|$)|/.*)",
    "^/404$",
    "^/onboarding/?.*$",
    "^/profile/.*$",
    "^/scoring($|\\?|/).*",
    "^/companies/.+$",
    "^(/auth)?/(login|signup)((/.*)*|\\?.*)$",
    "^/auth/(forgot_password|reset_password)/?(\\?.*|$)",
    "^/work/reset_password/(.*|$)",
    "^/x/reset_password/(.*|$)",
    "^/[^/]*/activity/?(\\?.*|$)",
    "^/work/sourcing($|\\?|/).*",
    "^/work/404($|\\?|/).*",
    "^/work/pricing-plans($|\\?|/).*",
    "^/work/iframe($|\\?|/).*",
    "^/work/subscribe-now($|\\?|/).*"
  ]
}
;
      HR.CKEDITOR_URL = "https://hrcdn.net/ckeditor/v4.11.4.2/ckeditor.js"
    </script>


    
  <script src="./product_files/base-153aa897c88730d6cee3642e04e184fceac798cf87b7ab79552102930ff30e59.js.download"></script>



    <script src="./product_files/hackerrank_libraries-1287800a7b053b1a92190bfa002e103edd55b7b39c6762b726a5751c1994f580.js.download" crossorigin="anonymous"></script>
    <script src="./product_files/codeshell-c2a21e50c1d9bcbc3177f15b19f1b5237be3f4cc4833dc610d04f23180f98c5b.js.download" crossorigin="anonymous"></script>
    <script src="./product_files/hackerrank-091374e2b1e8b26982a115c817b1fbed3b25ebe65e6ea58a905e504316ba0b06.js.download" crossorigin="anonymous"></script>
    <script src="./product_files/set-manifest-43521ec957bc6ed66f0adfeb06022b8497dfaf57.js.download" crossorigin="anonymous"></script>
    <script src="./product_files/require-347a93ee81566ec218dbb0c715ef65c45b1bc692fa0dfdf7189dce06cbf085b3.js.download" crossorigin="anonymous"></script>
    <script src="./product_files/dashboard-04cb90bc8664936819d2d335dc43aa525e7f428907b018d24e9f3f4e535ccda0.js.download" crossorigin="anonymous"></script>




<!-- jsCookies -->


<script type="text/javascript">
  window.extern_script_delay = 0;
  if (window.PRODUCT_NAMESPACE === 'hackerrank' && typeof($) === "function") {
    $(window).on("load", function(){
      if (('performance' in window) && ('timing' in window.performance)) {
        dom_time = window.performance.timing.domInteractive - window.performance.timing.navigationStart;
        if (dom_time > 12000) {
          window.extern_script_delay = 3000;
        } else if (dom_time > 7000) {
          window.extern_script_delay = 2000;
        } else if (dom_time > 6000) {
          window.extern_script_delay = 1000;
        }
      }
    });
  }
</script>

<script>
</script>

<script>
</script>

<!-- Google Analytics -->
<script type="text/javascript">
  $(window).on("load", function() {
    setTimeout(function() {
    (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();
    }, window.extern_script_delay);
  });
</script>

<!-- Mixpanel Stub -->
<script type="text/javascript">
  window.mixpanel = window.mixpanel || [];
  var attrs = "disable track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.set_once people.increment people.append people.track_charge people.clear_charges people.delete_user".split(" ");
  for (var attribute in attrs) {
      mixpanel[attrs[attribute]] = function () {};
  }
</script>

<script type="text/javascript">
  if (window.dataLayer) {
      const gaUserId = '520b31a4e4930a814ea1de0859d35bf8681c8d54';
      dataLayer.push({'event': 'identify', 'gaUserId': gaUserId});

      dataLayer.push({'event': 'setUserProps', 'userProps': {
        level: '1',
        badges_onboarding_status: '',
        jobs_consent: ''
      }});
  }
</script>

    <!-- End of hackerrank Zendesk Widget script -->

<!-- Filepicker -->
<script type="text/javascript">
  $(window).on("load", function() {
    setTimeout(function() {
    (function(a){if(window.filepicker){return}var b=a.createElement("script");b.type="text/javascript";b.async=!0;b.src=("https:"===a.location.protocol?"https:":"http:")+"//api.filepicker.io/v2/filepicker.js";var c=a.getElementsByTagName("script")[0];c.parentNode.insertBefore(b,c);var d={};d._queue=[];var e="pick,pickMultiple,pickAndStore,read,write,writeUrl,export,convert,store,storeUrl,remove,stat,setKey,constructWidget,makeDropPane".split(",");var f=function(a,b){return function(){b.push([a,arguments])}};for(var g=0;g<e.length;g++){d[e[g]]=f(e[g],d._queue)}window.filepicker=d})(document);
    filepicker.setKey("ApehXMbvXTWqWab7OmMr9z");
    }, window.extern_script_delay);
  });
</script>

<script type="text/javascript">
  window._fbq = window._fbq || [];
</script>

<!-- bizible -->
<script>
  $(window).on("load", function() {
    setTimeout(function() {
    (function(d, t) {
      var g = d.createElement(t),
          s = d.getElementsByTagName(t)[0];
      g.src = '//cdn.bizible.com/scripts/bizible.js';
      s.parentNode.insertBefore(g, s);
    }(document, 'script'));
    }, window.extern_script_delay);
  });
</script>


<script type="text/javascript">

    !function(obj){window.hr_metrics=obj,obj.loaded=!0,obj.config=obj.config||{},obj._b=obj._b||[],obj.init=function(options){this.config=$.extend({product:null,use_cookie:!1,uid_cookie_key:null,session_cookie_key:null,session_id:null,uid_token:null,uid_token_cookie_key:null,uid:Math.floor(1e12*(1+Math.random())).toString(16),metrics_endpoint:null,batch_track_interval:2e3,enable_gtm:!1},this.config||{},options||{})},obj.get_session_id=function(){return this.config.session_id?this.config.session_id:this.config.session_cookie_key?$.cookie(this.config.session_cookie_key):null},obj.get_uid_data=function(){return this.config.use_cookie?{uid:$.cookie(this.config.uid_cookie_key),uid_token:$.cookie(this.config.uid_token_cookie_key)}:{uid:this.config.uid,uid_token:this.config.uid_token}},obj.get_session_params=function(){var session_params={session_landing_url:$.cookie("session_landing_url"),session_referrer:$.cookie("session_referrer"),session_referring_domain:$.cookie("session_referring_domain")};try{var utm_params=$.cookie("session_utm_params");utm_params&&(utm_params=JSON.parse(utm_params),session_params.session_utm_source=utm_params.s,session_params.session_utm_medium=utm_params.m,session_params.session_utm_campaign=utm_params.c)}catch(e){}return session_params},obj.track=function(event_name,event_value,attrs,use_beacon){var common_attrs={session_id:this.get_session_id()},_tracking_data=(attrs=$.extend({},attrs,common_attrs,this.get_session_params()),$.extend({product:this.config.product,event_name:event_name,event_value:event_value,params:attrs},this.get_uid_data()));this._post_tracking_data(_tracking_data,use_beacon),this._push_to_gtm(event_name,event_value,attrs)},obj.batch_track=function(event_name,event_value,attrs){this._EVENT_ARRAY=this._EVENT_ARRAY||[];var that,common_attrs={session_id:this.get_session_id()},_tracking_data={event_name:event_name,event_value:event_value,params:attrs=$.extend({},attrs,common_attrs)};this._EVENT_ARRAY.push({time:(new Date).getTime(),url:document.location.href,track_data:_tracking_data}),this._event_batch_track_id||(this._event_batch_track_id=window.setInterval((that=this,function(){that.batch_track_record()}),this.config.batch_track_interval)),this._push_to_gtm(event_name,event_value,attrs)},obj.batch_track_record=function(use_beacon){if("object"==typeof this._EVENT_ARRAY&&this._EVENT_ARRAY.length>0){var _tracking_data_array=this._EVENT_ARRAY;this._EVENT_ARRAY=[];var _tracking_data=$.extend({product:this.config.product,batch_request:"true",current_time:(new Date).getTime(),data_array:JSON.stringify(_tracking_data_array),session_params:JSON.stringify(this.get_session_params())},this.get_uid_data());this._post_tracking_data(_tracking_data,use_beacon)}},obj._post_tracking_data=function(data,use_beacon){var metrics_endpoint=this.config.metrics_endpoint;if(!0===use_beacon&&"object"==typeof window.navigator&&"function"==typeof window.navigator.sendBeacon){var jsonContent="params_stream="+encodeURIComponent(JSON.stringify(data)),_json_blob=new Blob([jsonContent],{type:"application/x-www-form-urlencoded; charset=UTF-8"});window.navigator.sendBeacon(metrics_endpoint,_json_blob)}else $.ajax({type:"POST",url:metrics_endpoint,crossDomain:!0,xhrFields:{withCredentials:!0},beforeSend:function(){return!0},data:data})},obj._push_to_gtm=function(event_name,event_value,attrs){this.config.enable_gtm&&window.dataLayer&&window.dataLayer.push({event:"track",eventName:event_name,eventValue:event_value,eventAttrs:attrs})},function(o){if(Array.isArray(o._b)){for(var i=0;i<o._b.length;i++){var e=o._b[i];o[e[0]]&&"function"==typeof o[e[0]]&&o[e[0]].apply(o,e[1])}o._b=[]}}(obj)}(window.hr_metrics||{});

  (function() {
    hr_metrics.init({
      product: 'hackerrank',
      use_cookie: true,
      uid_cookie_key: 'hackerrank_mixpanel_token',
      uid_token_cookie_key: 'metrics_user_identifier',
      session_cookie_key: 'session_id',
      metrics_endpoint: 'https://metrics.hackerrank.com/metrics',
      enable_gtm: true
    });
  })();

  //tracking hrutm_ parameters
  $(window).on("load", function() {
    (function(){
      var sPageURL = window.location.search.substring(1);
      var sURLVariables = sPageURL.split('&');
      var trackingData;
      for(var i = 0; i < sURLVariables.length; i++) {
        var sParameterName = sURLVariables[i].split('=');
        if(sParameterName[0] == 'utm_source') {
          trackingData = decodeURIComponent(escape(sParameterName[1]));
          hr_metrics.batch_track(trackingData.event_name, trackingData)
        } else if (sParameterName[0] == 'ad-campaign' && sParameterName[1]=='Mkt1010415') {
          if(typeof HR !== "undefined" && HR !== null && (!HR.PREFETCH_DATA.profile || !HR.PREFETCH_DATA.profile.created_at)){
            document.cookie = "fb_ad_campaign_source="+sParameterName[1]+";path=/";
          }
        }
      }
    })();

    if(typeof HR !== "undefined" && HR !== null && HR.PREFETCH_DATA && HR.PREFETCH_DATA.profile &&  HR.PREFETCH_DATA.profile.created_at) {
      if($.cookie('fb_ad_campaign_source')) {
        window._fbq.push(['track', '6023409928156', {'value':'0.01','currency':'USD'}]);
        $.removeCookie('fb_ad_campaign_source', { path: '/' });
      }
    }
  });
</script>

  <script type="text/javascript">
    window.hr_metrics_extension_track = true;

      !function(obj){window.hr_metrics=obj,obj.externalService=function(event_type,event_value,attrs,service){(attrs=void 0!==attrs?attrs:{}).session_id=this.get_session_id(),service=void 0!==service?service:"mixpanel:heap",external_services=service.split(":")},obj.app_track=function(key,attrs){window.APP_METRICS=window.APP_METRICS||[],common_attrs={uid:$.cookie("hackerrank_mixpanel_token")},attrs=$.extend({},attrs,common_attrs),window.APP_METRICS.push({key:key,meta_data:attrs}),window.app_track_interval_id||(window.app_track_interval_id=window.setInterval(hr_metrics._send_app_track_data,5e3))},obj._send_app_track_data=function(){if(window.APP_METRICS&&window.APP_METRICS.constructor===Array&&!(window.APP_METRICS.length<=0)){var track_data={data:window.APP_METRICS};window.APP_METRICS=[];var metrics_endpoint="https://metrics.hackerrank.com/app_metrics";window.HR&&window.HR.development&&(metrics_endpoint="/app_metrics"),"function"==typeof moment&&"function"==typeof moment.tz&&(track_data.local_timezone=moment.tz.guess()),track_data.default_cdn_url=jsCookies.get("default_cdn_url"),track_data.document_referrer=document.referrer,$.ajax({type:"POST",url:metrics_endpoint,crossDomain:!0,xhrFields:{withCredentials:!0},beforeSend:function(){return!0},data:JSON.stringify(track_data),dataType:"json",contentType:"application/json"})}},obj.track_dwell_time=function(pathname,use_beacon){if(this._navigation_data&&this._navigation_data.page==pathname){var time_now=(new Date).getTime();this.batch_track("DwellTime",pathname,{attribute7:parseInt((time_now-(this._navigation_data.time||time_now))/1e3)},use_beacon)}},obj.set_navigation_data=function(pathname){this._navigation_data={page:pathname||document.location.pathname,time:(new Date).getTime()}},window.APP_METRIC_TRACKING_ENABLED&&"performance"in window&&"timing"in window.performance&&$(window).on("load",function(){setTimeout(function(){if(timing=window.performance.timing,obj={referring_url:window.location.pathname,fullLoadTime:timing.loadEventEnd-timing.navigationStart,loadTime:timing.loadEventEnd-timing.fetchStart,domReadyTime:timing.domComplete-timing.domInteractive,readyStart:timing.fetchStart-timing.navigationStart,redirectTime:timing.redirectEnd-timing.redirectStart,appcacheTime:timing.domainLookupStart-timing.fetchStart,unloadEventTime:timing.unloadEventEnd-timing.unloadEventStart,lookupDomainTime:timing.domainLookupEnd-timing.domainLookupStart,connectTime:timing.connectEnd-timing.connectStart,requestTime:timing.responseEnd-timing.requestStart,initDomTreeTime:timing.domInteractive-timing.responseEnd,loadEventTime:timing.loadEventEnd-timing.loadEventStart},"navigation"in window.performance&&"getEntries"in window.performance&&(obj.navigationType=window.performance.navigation.type,obj.navigationRedirectCount=window.performance.navigation.redirectCount,obj.fullLoadTime>8e3))try{var entries=window.performance.getEntries();entries[0].toJSON&&(obj.networkRequests=entries.map(function(e){return e.toJSON()}))}catch(e){}hr_metrics.app_track("page-load-metrics",obj)},1e3)}),$(window).on("load",function(){var _pathname=document.location.pathname,cdn_url_switched=jsCookies.get("cdn_url_switched");""!==cdn_url_switched&&jsCookies.destroy("cdn_url_switched"),hr_metrics.batch_track("PageLoad",_pathname+document.location.search,{attribute1:_pathname,attribute6:cdn_url_switched,cdn_url:jsCookies.get("cdn_url")})})}(window.hr_metrics||{}),"function"==typeof $&&window.hr_metrics_extension_track&&$(window).on("load",function(){var _pathname=document.location.pathname;hr_metrics.track_dwell_time&&(hr_metrics.track_dwell_time(_pathname),hr_metrics.set_navigation_data()),$(window).on("beforeunload",function(){var _pathname=document.location.pathname;hr_metrics.batch_track("PageClose",_pathname+document.location.search,{attribute2:_pathname},!0),hr_metrics.track_dwell_time&&hr_metrics.track_dwell_time(_pathname,!0),window.typingTimeout&&(window.clearTimeout(window.typingTimeout),window.triggerTypingEvent&&window.typingEventEnabled&&window.triggerTypingEvent()),hr_metrics.batch_track_record(!0)})});
  </script>

<!-- Load Facebook SDK for JavaScript -->
<script>
;(function(){
  // Function to have a list of functions to load on fbAsyncInit
  var toLoad = []
  window.fbReady = function(func){
    if( typeof func === 'function') {
      if( window.FB ) {
        func.call(window)
      } else {
        toLoad.push(func)
      }
    }
  }

  window.fbAsyncInit = function() {
    FB.init({
      appId      : '347499128655783',
      xfbml      : true,
      version    : 'v2.5',
      caption    : 'HackerRank.com',
    });

    // Execute all the fbAsyncInit functions
    toLoad.forEach(function(func){
      func.call(window)
    })
  };
})();
/*
$(window).on("load", function() {
  setTimeout(function() {
    (function(d, s, id){
       var js, fjs = d.getElementsByTagName(s)[0];
       if (d.getElementById(id)) {return;}
       js = d.createElement(s); js.id = id;
       js.src = "//connect.facebook.net/en_US/sdk.js";
       fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
  }, window.extern_script_delay);
});
*/
</script>
<!-- Load Twitter SDK for JavaScript -->
<script>
window.twttr = (function() {
  t = window.twttr || {};
  if (typeof t.ready === 'undefined') {
    t._e = [];
    t.ready = function(f) {
      t._e.push(f);
    };
  }
  return t;
})();
$(window).on("load", function() {
  setTimeout(function() {
    (function(d, s, id){
       var js, fjs = d.getElementsByTagName(s)[0];
       if (d.getElementById(id)) {return;}
       js = d.createElement(s); js.id = id;
       js.src = "https://platform.twitter.com/widgets.js";
       fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'twitter-wjs'));
  }, window.extern_script_delay);
});
</script>

<script type="text/javascript">
    if (typeof($) == "function") {
        $(document).ready(function() {
            function we_are_hiring() {
                lines = [
                    "===============================================================================",
                    ",--.  ,--.              ,--.                 ,------.                 ,--.     ",
                    "|  '--'  | ,--,--. ,---.|  |,-. ,---. ,--.--.|  .--. ' ,--,--.,--,--, |  |,-.  ",
                    "|  .--.  |' ,-.  || .--'|     /| .-. :|  .--'|  '--'.'' ,-.  ||      \\|     /  ",
                    "|  |  |  |\\ '-'  |\\ `--.|  \\  \\\\   --.|  |   |  |\\  \\ \\ '-'  ||  ||  ||  \\  \\  ",
                    "`--'  `--' `--`--' `---'`--'`--'`----'`--'   `--' '--' `--`--'`--''--'`--'`--' ",
                    "===============================================================================",
                    "  You opened the console! Know some code, do you? Want to work for one of the  ",
                    "  best startups around? https://www.hackerrank.com/careers                     ",
                    "==============================================================================="
                ]
                for (i = 0; i < lines.length; i ++) {
                    console.log(lines[i]);
                }
            }
            setTimeout(we_are_hiring, 5000);
            if(window.trackJs) {
              trackJs.track("Page Loaded");
            }
        });
    }
</script>

<!-- Some Black Magic for Internet Explorer -->

<!--[if lt IE 10]>
<script src="https://hrcdn.net/hackerrank/assets/jquery-plugins/jQuery.XDomainRequest-bbf1203faae294b74f7077ea5bad499fabba38e298f8cd8cbd9fbdd8248c129b.js"></script>
<![endif]-->

<!--[if lt IE 9]>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.6/html5shiv.min.js" type="text/javascript"></script>
<![endif]-->

<!-- Chrome Frame for IE6 -->
<!--[if lt IE 7 ]>
 <script src="https://ajax.googleapis.com/ajax/libs/chrome-frame/1.0.2/CFInstall.min.js"></script><script>window.attachEvent("onload",function(){CFInstall.check({mode:"overlay"})})</script>
<![endif]-->

<!--[if lte IE 9]>
<script>
    IE_BROWSER = true
</script>
<![endif]-->

<!-- Track button clicks -->
<script type="text/javascript">
    $(document).on('click', 'a, button, input, select, i', null, function(e) {
        var src = e.currentTarget, $src = $(e.currentTarget);
        if ($src.attr('data-analytics')) {
            action = 'Click'; data = $src.attr('data-analytics');
        } else {
            return;
        }

            hr_metrics.batch_track(action, data, (function() {
                var params={};
                for (var _i=1; _i<=12; ++_i){
                    var _attr = 'data-attr'+_i;
                    if ($src.attr(_attr)){
                        params['attribute'+_i] = $src.attr(_attr);
                }}
                var attributes = src.attributes, attr_length = src.attributes.length;
                for (var i = 0; i < attr_length; i++){
                  var attribute = attributes[i];
                  if (attribute.name.indexOf('data-attr-') === 0){
                    param_name = attribute.name.substr('data-attr-'.length);
                    if (param_name.length > 0) {
                      params[param_name] = attribute.value;
                    }
                  }
                }
                return params;
            })());
        // google analytics
        _gaq.push(['_trackEvent', 'Events' , action, data])
    });

    $(document).on('AnalyticsEvent', function(e) {
        action = e.event_type || false
        data = e.event_name || false

        if (!action || !data)
          return

        params = {}
        params['attribute1'] = e.event_value || ""
        params['attribute7'] = e.integer_event_value

        if (window.HR && window.HR.current_page)
          params['attribute2'] = window.HR.current_page

        if (window.HR && window.HR.current_contest)
          params['attribute3'] = window.HR.current_contest.get('name')

            hr_metrics.batch_track(action, data, params);
        // google analytics
        _gaq.push(['_trackEvent', 'Events' , action, data])
    });
</script>


<!-- Google Tag Manager (noscript) #1 -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5FXW96J"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) #1 -->



<div class="offline-ui offline-ui-up"><div class="offline-ui-content"></div><a href="https://www.hackerrank.com/" class="offline-ui-retry"></a></div><div class="offline-ui offline-ui-up"><div class="offline-ui-content"></div><a href="https://www.hackerrank.com/" class="offline-ui-retry"></a></div><iframe scrolling="no" frameborder="0" allowtransparency="true" src="./product_files/widget_iframe.2b2d73daf636805223fb11d48f3e94f7.html" title="Twitter settings iframe" style="display: none;"></iframe><iframe name="filepicker_comm_iframe" id="filepicker_comm_iframe" src="./product_files/saved_resource.html" style="display: none;"></iframe><iframe name="fpapi_comm_iframe" id="fpapi_comm_iframe" src="./product_files/saved_resource(1).html" style="display: none;"></iframe><img alt="" src="./product_files/ipv" style="display: none;"><img alt="" src="./product_files/u" style="display: none;"><iframe id="rufous-sandbox" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" style="position: absolute; visibility: hidden; display: none; width: 0px; height: 0px; padding: 0px; border: none;" title="Twitter analytics iframe" src="./product_files/saved_resource(2).html"></iframe><link rel="stylesheet" href="./product_files/animate-4419fe561f5717d2a2bb1df0c40ec5dc1b1fbfeb311b2493b134f53158bcad52.css" media="all"><img alt="" src="./product_files/ipv(1)" style="display: none;"><ul class="vakata-context"></ul><div id="jstree-marker" style="display: none;">&nbsp;</div><img alt="" src="./product_files/ipv(2)" style="display: none;"><img alt="" src="./product_files/ipv(3)" style="display: none;"><img alt="" src="./product_files/ipv(4)" style="display: none;"><img alt="" src="./product_files/ipv(5)" style="display: none;"><div class="select2-drop select2-display-none select2-drop-active select2-with-searchbox" style="display: none; top: 1438px; left: 1027.88px; width: 220px;">   <div class="select2-search">       <input type="text" autocomplete="off" autocorrect="off" autocapitilize="off" spellcheck="false" class="select2-input" fdprocessedid="sxfaup">   </div>   <ul class="select2-results"></ul></div><img alt="" src="./product_files/ipv(6)" style="display: none;"><img alt="" src="./product_files/ipv(7)" style="display: none;"><img alt="" src="./product_files/ipv(8)" style="display: none;"><img alt="" src="./product_files/ipv(9)" style="display: none;"><img alt="" src="./product_files/ipv(10)" style="display: none;"><img alt="" src="./product_files/ipv(11)" style="display: none;"><img alt="" src="./product_files/ipv(12)" style="display: none;"><img alt="" src="./product_files/ipv(13)" style="display: none;"><img alt="" src="./product_files/ipv(14)" style="display: none;"><img alt="" src="./product_files/ipv(15)" style="display: none;"><img alt="" src="./product_files/ipv(16)" style="display: none;"><img alt="" src="./product_files/ipv(17)" style="display: none;"><img alt="" src="./product_files/ipv(18)" style="display: none;"><img alt="" src="./product_files/ipv(19)" style="display: none;"><img alt="" src="./product_files/ipv(20)" style="display: none;"><img alt="" src="./product_files/ipv(21)" style="display: none;"><div id="select2-drop-mask" class="select2-drop-mask" style="width: 1519px; height: 1916px; display: none;"></div><div class="select2-drop select2-display-none select2-drop-active select2-with-searchbox" style="display: none; top: 1380px; left: 1027.88px; width: 220px;">   <div class="select2-search">       <input type="text" autocomplete="off" autocorrect="off" autocapitilize="off" spellcheck="false" class="select2-input" fdprocessedid="0yt1j">   </div>   <ul class="select2-results"></ul></div><img alt="" src="./product_files/ipv(22)" style="display: none;"><img alt="" src="./product_files/ipv(23)" style="display: none;"><img alt="" src="./product_files/ipv(24)" style="display: none;"><img alt="" src="./product_files/ipv(25)" style="display: none;"><img alt="" src="./product_files/ipv(26)" style="display: none;"><img alt="" src="./product_files/ipv(27)" style="display: none;"><img alt="" src="./product_files/ipv(28)" style="display: none;"><img alt="" src="./product_files/ipv(29)" style="display: none;"><img alt="" src="./product_files/ipv(30)" style="display: none;"><img alt="" src="./product_files/ipv(31)" style="display: none;"><img alt="" src="./product_files/ipv(32)" style="display: none;"><img alt="" src="./product_files/ipv(33)" style="display: none;"><img alt="" src="./product_files/ipv(34)" style="display: none;"><img alt="" src="./product_files/ipv(35)" style="display: none;"><img alt="" src="./product_files/ipv(36)" style="display: none;"><img alt="" src="./product_files/ipv(37)" style="display: none;"><img alt="" src="./product_files/ipv(38)" style="display: none;"><img alt="" src="./product_files/ipv(39)" style="display: none;"><img alt="" src="./product_files/ipv(40)" style="display: none;"><img alt="" src="./product_files/ipv(41)" style="display: none;"><img alt="" src="./product_files/ipv(42)" style="display: none;"><img alt="" src="https://cdn.bizible.com/m/ipv?_biz_r=https%3A%2F%2Fwww.hackerrank.com%2Fcontests%2Ft1-aiml2023%2Fchallenges%2Fbasic-calculator-1%2Fsubmissions%2Fcode%2F1356477371&amp;_biz_h=805002629&amp;_biz_u=ec0ed0bdbe964fe9be4ce1e1795b4f6f&amp;_biz_s=3c0f34&amp;_biz_l=https%3A%2F%2Fwww.hackerrank.com%2Fcontests%2Ft1-aiml2023%2Fchallenges%2Fbasic-calculator-1&amp;_biz_t=1676569696399&amp;_biz_i=Product%20of%202%20numbers%20%7C%20T1_aiml2023%20Question%20%7C%20Contests%20%7C%20HackerRank&amp;_biz_n=43&amp;rnd=725442&amp;cdn_o=a&amp;_biz_z=1676569696400" style="display: none;"><img alt="" src="https://cdn.bizible.com/m/ipv?_biz_r=https%3A%2F%2Fwww.hackerrank.com%2Fcontests%2Ft1-aiml2023%2Fchallenges%2Fbasic-calculator-1&amp;_biz_h=805002629&amp;_biz_u=ec0ed0bdbe964fe9be4ce1e1795b4f6f&amp;_biz_s=3c0f34&amp;_biz_l=https%3A%2F%2Fwww.hackerrank.com%2Fcontests%2Ft1-aiml2023%2Fchallenges&amp;_biz_t=1676569698250&amp;_biz_i=Product%20of%202%20numbers%20%7C%20T1_aiml2023%20Question%20%7C%20Contests%20%7C%20HackerRank&amp;_biz_n=44&amp;rnd=272834&amp;cdn_o=a&amp;_biz_z=1676569698251" style="display: none;"><span role="status" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></span><img alt="" src="https://cdn.bizible.com/m/ipv?_biz_r=https%3A%2F%2Fwww.hackerrank.com%2Fcontests%2Ft1-aiml2023%2Fchallenges&amp;_biz_h=805002629&amp;_biz_u=ec0ed0bdbe964fe9be4ce1e1795b4f6f&amp;_biz_s=3c0f34&amp;_biz_l=https%3A%2F%2Fwww.hackerrank.com%2Fcontests%2Ft1-aiml2023%2Fchallenges%2Fvowel-or-consonant-1-1&amp;_biz_t=1676569712237&amp;_biz_i=Vowel%20or%20Consonant%201%20%7C%20T1_aiml2023%20Question%20%7C%20Contests%20%7C%20HackerRank&amp;_biz_n=45&amp;rnd=487928&amp;cdn_o=a&amp;_biz_z=1676569712238" style="display: none;"></body><!-- Load Jquery --></html>