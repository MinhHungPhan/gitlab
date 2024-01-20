<?php
/**
 * Created by PhpStorm.
 * User: gaces
 * Date: 01/08/16
 * Time: 15:32
 */

define('HTML_EOL', '<br>');

class RedmineInteractor
{
    CONST REDMINE_API_KEY = '885799aafae9ab0d60706fbbbc2f0d671f100430'; //GACES
    CONST REDMINE_BASE_URL = 'https://redmine-projets.smile.fr/';
    CONST REDMINE_PROJECT_IDS = [7840, 9211, 9210, 9212];
    CONST CODE_REVIEW_OK_STATUS = 57;
    CONST EMAIL_DEST = 'gaces@smile.fr';

    private $issues;
    private $hasError = false;

    /**
     * @param String $url
     * @param bool $expectContent
     * @param bool $raw
     * @return mixed|null|SimpleXMLElement
     */
    public function curl($url, $expectContent = true, $raw = false)
    {
        usleep(100);
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $url);
        if ($expectContent) {
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        }

        $result = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

        $valid = $expectContent ? $result && $httpCode == 200 : $httpCode == 200;

        if (!$valid) {
            echo "Nothing found for url: $url\n";
            return null;
        }

        curl_close($ch);

        if ($expectContent && !$raw) {
            return simplexml_load_string($result);
        }
        else {
            return $result;
        }
    }

    /**
     *
     */
    private function getIssuesToProcess()
    {
        $url = self::REDMINE_BASE_URL
            . '/issues.xml?'
            . 'key=' . self::REDMINE_API_KEY
            . '&set_filter=1'
            . '&utf8=%E2%9C%93'
            . '&f%5B%5D=status_id'
            . '&f%5B%5D=project_id'
            . '&op%5Bstatus_id%5D=%3D'
            . '&op%5Bproject_id%5D=%3D'
            . '&v%5Bstatus_id%5D%5B%5D=' . self::CODE_REVIEW_OK_STATUS;

        foreach (self::REDMINE_PROJECT_IDS as $id) {
            $url .= '&v%5Bproject_id%5D%5B%5D=' . $id;
        }

        $issues = $this->curl($url);
        if ($issues === null) {
            echo "No issue in the specified status found";
            exit(0);
        }

        foreach ($issues as $issue) {
            $this->issues[$issue->id->__toString()] = $issue->subject->__toString();
        }
    }

    /**
     * Send email
     */
    private function sendMail()
    {
        $status = $this->hasError ? 'KO' : 'OK';
        $body = 'Hello,
        The delivery on integration is ' . $status . PHP_EOL;

        if (count($this->issues) > 0) {
            $body .= 'tickets delivered :' . PHP_EOL;

            foreach ($this->issues as $id => $title) {
                $body .= "- $title (" . self::REDMINE_BASE_URL . "/issues/$id)" . PHP_EOL;
            }
        } else {
            $body .= 'No tickets delivered' . PHP_EOL;
        }

        $body .= PHP_EOL . 'Regards' . PHP_EOL;
        $headers[] = 'Content-Type: text/plain; charset=utf-8';

        $status = mail(
            self::EMAIL_DEST,
            '[ASTORE] Automatic integration delivery ' . date("Y-m-d H:i:s") . " $status",
            $body,
            implode("\r\n", $headers)
        );

        if (!$status) {
            echo "ERROR: Begin email not sent";
        }
    }

    private function checkServerStatus()
    {
        if ($this->curl('https://www-in01.astoreshop.aws.smile.fr/health_check.php', false) === null) {
            $this->hasError = true;
        }
    }

    /**
     * Process
     */
    public function process()
    {
        $this->getIssuesToProcess();
        $this->checkServerStatus();
        $this->sendMail();
    }
}

$o = new RedmineInteractor();
$o->process();
